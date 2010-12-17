#!/bin/bash

# 

## FIXME: Find some other place for these dirs

if [ ! -d /tmp/drives ]; then
  mkdir /tmp/drives
fi

if [ ! -d /tmp/fstab.d ]; then
  mkdir /tmp/fstab.d
fi

#
# helper functions
#

UDEVLOCKFILE="/tmp/.udevlock"

#
# Simple locking function
#

my_lockfile ()
{
  TEMPFILE="$1.$$"
  LOCKFILE="$1.lock"

  { echo $$ > ${TEMPFILE}; } &> /dev/null || {
    return 1;
  }
  ln ${TEMPFILE} ${LOCKFILE} &> /dev/null && {
    rm -f ${TEMPFILE}
    return 0;
  }
  kill -0 `cat ${LOCKFILE}`  &> /dev/null && {
    rm -f ${TEMPFILE}
    return 1;
  }
  rm -f ${LOCKFILE}
  ln ${TEMPFILE} ${LOCKFILE} &> /dev/null && {
    rm -f ${TEMPFILE}
    return 0;
  }
  rm -f ${TEMPFILE}
  return 1
}

#
# Obtain lock
#

obtain_lock ()
{
  until my_lockfile ${UDEVLOCKFILE} ; do
    sleep 1
  done
}

#
# Release lock
#

release_lock ()
{
  rm -f ${UDEVLOCKFILE}.lock
}

#
# combine the fstab files into a master fstab
#

combine_fstabs ()
{
  :> /tmp/fstab
  for TABFILE in /tmp/fstab.d/*
  do
    if [ -f ${TABFILE} ] ; then
      cat ${TABFILE} >> /tmp/fstab
    fi
  done
}

#
# Begin work
#

LTSP_DEVTYPE="none"

case ${DEVNAME} in
  /dev/*/lun0/disc)  LTSP_DEVTYPE="floppy"
                     ;;
  /dev/fd*)          LTSP_DEVTYPE="floppy"
                     ;;
  /dev/*/cd)         LTSP_DEVTYPE="cdrom"
                     ;;
  /dev/*/part*)      LTSP_DEVTYPE="disk"
                     ;;
  /dev/sd*)          LTSP_DEVTYPE="disk"    # unpartitioned sticks: thx Gadi
                     ;;

esac
  
logger "udev detected ${ACTION} of ${LTSP_DEVTYPE}"

if [ "${LTSP_DEVTYPE}" = "none" ]; then
  exit 0
fi

obtain_lock

if [ "${ACTION}" = "add" ]; then

  #
  # Run the vol_id command if this isn't a cdrom, as it's therefore a memory
  # stick. 
  #
  
  if [ "${LTSP_DEVTYPE}" = "disk" ]; then
    eval `/lib/udev/vol_id --export "${DEVNAME}" | \
          sed -e "s/\(.*\)=\(.*\)/\1=\"\2\"/"`
  
    if [ "${ID_FS_USAGE}" != "filesystem" -a \
         "${ID_FS_USAGE}" != "disklabel" ] ; then
      release_lock
      exit 0
    fi
  fi
  
  #
  # Calculate the size of the volume
  #
  
  BLOCKS=${1:-"0"}
  
  SIZE=$((${BLOCKS} * 512 / 1048576))
  
  #
  # use the volume label as the mountpoint name.  If the volume doesn't
  # have a label, make a fake one
  #
  
  case ${LTSP_DEVTYPE} in
    floppy)  MOUNTPOINT="My_Floppy"
             DESCRIPTION="Floppy"
             ;;
    cdrom)   MOUNTPOINT="My_CDrom"
             DESCRIPTION="CDrom"
             ;;
    disk)    MOUNTPOINT=${ID_FS_LABEL_SAFE:-"Removable_Device_${SIZE}_Mb"}
             DESCRIPTION=${ID_FS_LABEL:-"Removable Device (${SIZE}Mb)"}
             ;;
  esac
  
  #
  # Multiple volume names the same.
  #
  
  if [ -f /tmp/fstab.d/${MOUNTPOINT} ] ; then
    for i in 2 3 4 5 6 7 8 9; do
      NEWMOUNTPOINT="${MOUNTPOINT}$i"
      if [ ! -f /tmp/fstab.d/${NEWMOUNTPOINT} ] ; then
        FOUND="yes"
        break
      fi
    done
    if [ "${FOUND}" = "yes" ] ; then
      MOUNTPOINT=${NEWMOUNTPOINT}
    else
      logger "$0 couldn't find a valid free mountpoint"
      exit 1
    fi
  fi
  
  #
  # Create the fstab entry.
  #
  
  MOUNTDIR="/tmp/drives/${MOUNTPOINT}"
  mkdir "${MOUNTDIR}"
  if [ "${LTSP_DEVTYPE}" = "cdrom" ]; then
    echo "${DEVNAME} ${MOUNTDIR} auto ro,utf8 0 0" > /tmp/fstab.d/${MOUNTPOINT}
    echo "AddCdromDrive|${MOUNTPOINT}|${DEVNAME}|${DESCRIPTION}" \
      > /tmp/lbus.fifo
  else
    # utf8 option needed for unicode characters
    if [ "$ID_FS_TYPE" == "vfat" ]; then
	OPTIONS="rw,utf8,noatime,shortname=mixed,quiet,sync"
    else
	OPTIONS="rw,noatime,sync"
    fi
    echo "${DEVNAME} ${MOUNTDIR} auto ${OPTIONS} 0 0" \
      > /tmp/fstab.d/${MOUNTPOINT}
    echo "AddBlockDevice|${MOUNTPOINT}|${DEVNAME}|0|${SIZE}|${DESCRIPTION}" \
      > /tmp/lbus.fifo
  fi

elif [ "${ACTION}" = "remove" ]; then

  for TABFILE in /tmp/fstab.d/*; do
    if [ -f ${TABFILE} ] ; then 
      read TDEV TDIR TTYPE TOPT TFREQ TPASS < ${TABFILE}
      if [ "${TDEV}" = "${DEVNAME}" ]; then
        MOUNTPOINT=`basename ${TDIR}`
        echo "RemoveDevice|${MOUNTPOINT}" > /tmp/lbus.fifo
        rm ${TABFILE}
	umount -f "${DEVNAME}"
        rmdir "${TDIR}"
      fi
    fi
  done

fi

#
# Cat together all the individual fstabs.
#

combine_fstabs

release_lock

exit 0
