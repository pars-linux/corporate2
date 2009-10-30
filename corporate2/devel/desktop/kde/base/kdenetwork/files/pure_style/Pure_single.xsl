<?xml version="1.0" encoding="UTF-8"?>
<!--
  'Pure' theme for Kopete
  Copyright (C) 2005, Francois Chazal <chazal_f@epita.fr>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html"/>
  <xsl:param name="appdata"/>
  <xsl:variable name="image-location"><xsl:value-of select="$appdata"/>Pure/</xsl:variable>


  <xsl:template match="message">
    <div class="KopeteMessage" style="padding: 5px;">
    <xsl:attribute name="id">
    <xsl:value-of select="@id"/>
    </xsl:attribute>

    <xsl:choose>


    <!-- Style for incoming messages =======================================-->

    <xsl:when test="@direction='0'">
      <div class="message">
      <xsl:attribute name="style">
        background: #c9d9f0 url(<xsl:value-of select="$image-location"/>corner-tl.png) no-repeat top left;
        margin-right: 6px; margin-left: 6px;
      </xsl:attribute>

        <!-- Title of the message - - - - - - - - - - - - - - - - - - - - - -->

        <div>
        <xsl:attribute name="style">
          background: url(<xsl:value-of select="$image-location"/>corner-tr.png) no-repeat top right;
          padding-left: 4px; padding-right: 4px;
          vertical-align: middle;
          line-height: 20px;
          height: 20px;
        </xsl:attribute>

          <span class="name">
          <xsl:attribute name="style">
            position: absolute;
            background: url(<xsl:value-of select="$image-location"/>contact.png) no-repeat center left;
            text-align: left; font-size: 10px; font-weight: bold; color: #567199;
            padding-right: 20px;
            padding-left: 20px;
            overflow: hidden;
            height: 20px;

          <xsl:if test="@importance='2'">
            background: url(<xsl:value-of select="$image-location"/>important.png) no-repeat center left;
          </xsl:if>
          </xsl:attribute>

            <kopete-i18n>%FROM_METACONTACT_DISPLAYNAME%</kopete-i18n>
          </span>

          <span class="time">
          <xsl:attribute name="style">
            position: relative;
            background: #c9d9f0 url(<xsl:value-of select="$image-location"/>clock.png) no-repeat center right;
            text-align: right; font-size: 10px; font-weight: bold; color: #567199;
            padding-right: 20px;
            padding-left: 5px;
            float: right;
            z-index: 1;
          </xsl:attribute>

            <xsl:value-of select="@time"/>
          </span>
        </div>

        <!-- Contents of the message  - - - - - - - - - - - - - - - - - - - -->

        <div>
        <xsl:attribute name="style">
          background: #ffffff url(<xsl:value-of select="$image-location"/>corner-bl.png) no-repeat bottom left;
          padding-bottom: 7px;
        </xsl:attribute>

        <xsl:attribute name="dir">
          <xsl:value-of select="body/@dir"/>
        </xsl:attribute>

          <div>
          <xsl:attribute name="style">
            background: #f5f6fa;
            padding: 5px;
            border-bottom: 2px solid #c9d9f0;
            overflow: auto;

          <xsl:if test="body/@color">
            color:<xsl:value-of select="body/@color"/>;
          </xsl:if>

          <xsl:if test="body/@bgcolor">
            background-color:<xsl:value-of select="body/@bgcolor"/>;
          </xsl:if>

          <xsl:if test="body/@font">
            font:<xsl:value-of select="body/@font"/>;
          </xsl:if>

          <xsl:if test="@importance='2'">
            font-weight: bold;
          </xsl:if>

          <xsl:if test="from/contact/@userPhoto">min-height: 56px;</xsl:if>
          </xsl:attribute>

            <xsl:if test="from/contact/@userPhoto">
              <img>
                <xsl:attribute name="src">
                  data:image/png;base64,<xsl:value-of select="from/contact/@userPhoto"/>
                </xsl:attribute>
                <xsl:attribute name="style">
                  float: left;
                  padding: 4px;
                  height: 48px;
                  margin-right: 4px;
                  padding-right: 8px;
                  border-right: 1px dotted #c0c0c0;
                </xsl:attribute>
              </img>
            </xsl:if>

            <xsl:value-of disable-output-escaping="yes" select="body"/>
          </div>
        </div>
      </div>
    </xsl:when>




    <!-- Style for outgoing messages =======================================-->

    <xsl:when test="@direction='1'">
      <div class="message">
      <xsl:attribute name="style">
        background: #e1e1e1 url(<xsl:value-of select="$image-location"/>corner-tl.png) no-repeat top left;
        margin-right: 6px; margin-left: 6px;
      </xsl:attribute>

        <!-- Title of the message - - - - - - - - - - - - - - - - - - - - - -->

        <div>
        <xsl:attribute name="style">
          background: url(<xsl:value-of select="$image-location"/>corner-tr.png) no-repeat top right;
          padding-left: 4px; padding-right: 4px;
          vertical-align: middle;
          line-height: 20px;
          height: 20px;
        </xsl:attribute>

          <span class="name">
          <xsl:attribute name="style">
            position: absolute;
            background: url(<xsl:value-of select="$image-location"/>myself.png) no-repeat center left;
            text-align: left; font-size: 10px; font-weight: bold; color: #707070;
            padding-right: 20px;
            padding-left: 20px;
            overflow: hidden;
            height: 20px;

          <xsl:if test="@importance='2'">
            background: url(<xsl:value-of select="$image-location"/>important.png) no-repeat center left;
          </xsl:if>
          </xsl:attribute>

            <kopete-i18n>%FROM_METACONTACT_DISPLAYNAME%</kopete-i18n>
          </span>

          <span class="time">
          <xsl:attribute name="style">
            position: relative;
            background: #e1e1e1 url(<xsl:value-of select="$image-location"/>clock.png) no-repeat center right;
            text-align: right; font-size: 10px; font-weight: bold; color: #707070;
            padding-right: 20px;
            padding-left: 5px;
            float: right;
            z-index: 1;
          </xsl:attribute>

            <xsl:value-of select="@time"/>
          </span>
        </div>

        <!-- Contents of the message  - - - - - - - - - - - - - - - - - - - -->

        <div>
        <xsl:attribute name="style">
          background: #ffffff url(<xsl:value-of select="$image-location"/>corner-br.png) no-repeat bottom right;
          padding-bottom: 7px;
        </xsl:attribute>

        <xsl:attribute name="dir">
          <xsl:value-of select="body/@dir"/>
        </xsl:attribute>

          <div>
          <xsl:attribute name="style">
            background: #f9f9f9;
            padding: 5px;
            border-bottom: 2px solid #e1e1e1;
            overflow: auto;

          <xsl:if test="body/@color">
            color:<xsl:value-of select="body/@color"/>;
          </xsl:if>

          <xsl:if test="body/@bgcolor">
            background-color:<xsl:value-of select="body/@bgcolor"/>;
          </xsl:if>

          <xsl:if test="body/@font">
            font:<xsl:value-of select="body/@font"/>;
          </xsl:if>

          <xsl:if test="@importance='2'">
            font-weight: bold;
          </xsl:if>

          <xsl:if test="from/contact/@userPhoto">min-height: 56px;</xsl:if>
          </xsl:attribute>

            <xsl:if test="from/contact/@userPhoto">
              <img>
                <xsl:attribute name="src">
                  data:image/png;base64,<xsl:value-of select="from/contact/@userPhoto"/>
                </xsl:attribute>
                <xsl:attribute name="style">
                  float: left;
                  padding: 4px;
                  height: 48px;
                  margin-right: 4px;
                  padding-right: 8px;
                  border-right: 1px dotted #c0c0c0;
                </xsl:attribute>
              </img>
            </xsl:if>

            <xsl:value-of disable-output-escaping="yes" select="body"/>
          </div>
        </div>
      </div>
    </xsl:when>




    <!-- Style for system messages =========================================-->

    <xsl:when test="@direction='2'">
      <div class="system_message">
      <xsl:attribute name="style">
        padding-left: 10px; padding-right: 10px;
        border-bottom: 1px dotted #c0c0c0;
        border-top: 1px dotted #c0c0c0;
        vertical-align: middle;
        line-height: 20px;
        height: 20px;
      </xsl:attribute>

        <span class="contents">
        <xsl:attribute name="style">
          position: absolute;
          background: url(<xsl:value-of select="$image-location"/>system.png) no-repeat center left;
          text-align: left; font-size: 10px; font-weight: bold; color: #808080;
          padding-right: 20px;
          padding-left: 20px;
          overflow: hidden;
          height: 20px;
          float: left;
        </xsl:attribute>

          <xsl:value-of disable-output-escaping="yes" select="body"/>
        </span>

        <span class="time">
        <xsl:attribute name="style">
          position: relative;
          background: #ffffff url(<xsl:value-of select="$image-location"/>clock.png) no-repeat center right;
          text-align: right; font-size: 10px; font-weight: bold; color: #808080;
          padding-right: 20px;
          padding-left: 5px;
          float: right;
          z-index: 1;
        </xsl:attribute>

          <xsl:value-of select="@time"/>
        </span>
      </div>
    </xsl:when>




    <!-- Style for action messages =========================================-->

    <xsl:when test="@direction='3'">
      <div class="system_message">
      <xsl:attribute name="style">
        padding-left: 10px; padding-right: 10px;
        border-bottom: 1px dotted #c0c0c0;
        border-top: 1px dotted #c0c0c0;
        vertical-align: middle;
        line-height: 20px;
        height: 20px;
      </xsl:attribute>

        <span class="contents">
        <xsl:attribute name="style">
          position: absolute;
          background: url(<xsl:value-of select="$image-location"/>action.png) no-repeat center left;
          text-align: left; font-size: 10px; font-weight: bold; color: #808080;
          padding-right: 20px;
          padding-left: 20px;
          overflow: hidden;
          height: 20px;
          float: left;
        </xsl:attribute>

          <xsl:value-of disable-output-escaping="yes" select="body"/>
        </span>

        <span class="time">
        <xsl:attribute name="style">
          position: relative;
          background: #ffffff url(<xsl:value-of select="$image-location"/>clock.png) no-repeat center right;
          text-align: right; font-size: 10px; font-weight: bold; color: #808080;
          padding-right: 20px;
          padding-left: 5px;
          float: right;
          z-index: 1;
        </xsl:attribute>

          <xsl:value-of select="@time"/>
        </span>
      </div>
    </xsl:when>

    </xsl:choose>
    </div>
  </xsl:template>
</xsl:stylesheet>
