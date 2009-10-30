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

<?Kopete Flag:TransformAllMessages?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html"/>
  <xsl:param name="appdata"/>

  <xsl:variable name="image-location"><xsl:value-of select="$appdata"/>Pure/</xsl:variable>


  <!-- Definition of the document ========================================-->

  <xsl:template match="document">
    <xsl:variable name="messages" select="message"/>

    <xsl:for-each select="message">
      <xsl:call-template name="process_message">
        <xsl:with-param name="messages" select="$messages"/>
      </xsl:call-template>
    </xsl:for-each>
  </xsl:template>




  <!-- Messages processing =================================================-->

  <xsl:template name="process_message">
    <xsl:param name="messages"/>


    <!-- Variables definition = = = = = = = = = = = = = = = = = = = = = = = -->

    <xsl:variable name="position" select="position()"/>

    <xsl:variable name="next" select="$messages[$position + 1]"/>
    <xsl:variable name="next_author" select="$next/from/contact/@contactId"/>

    <xsl:variable name="current" select="$messages[$position]"/>
    <xsl:variable name="current_author" select="$current/from/contact/@contactId"/>

    <xsl:variable name="previous" select="$messages[$position - 1]"/>
    <xsl:variable name="previous_author" select="$previous/from/contact/@contactId"/>


    <!-- Message group definition = = = = = = = = = = = = = = = = = = = = = -->

    <div class="message">


      <!-- Incoming or Outgoing messages  - - - - - - - - - - - - - - - - - -->

      <xsl:if test="(@direction='0') or (@direction='1')">
        <xsl:if test="not($previous_author = $current_author)">

          <xsl:attribute name="style">
            margin-right: 11px; margin-left: 11px;

            margin-top: 5px;
            margin-bottom: 10px;
          </xsl:attribute>

          <!-- Header of the message  - - - - - - - - - - - - - - - - - - - -->

          <div class="message_header">
            <xsl:attribute name="style">
              background: url(<xsl:value-of select="$image-location"/>corner-tl.png) no-repeat top left;

              <xsl:if test="@direction='0'">background-color: #c9d9f0;</xsl:if>
              <xsl:if test="@direction='1'">background-color: #e1e1e1;</xsl:if>
            </xsl:attribute>

            <div id="message_header2">
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
                  text-align: left; font-size: 10px; font-weight: bold;
                  padding-right: 20px;
                  padding-left: 20px;
                  overflow: hidden;
                  height: 20px;

                  <xsl:if test="@direction='0'">
                    background: url(<xsl:value-of select="$image-location"/>contact.png) no-repeat center left;
                    color: #567199;
                  </xsl:if>
                  <xsl:if test="@direction='1'">
                    background: url(<xsl:value-of select="$image-location"/>myself.png) no-repeat center left;
                    color: #707070;
                  </xsl:if>

                  <xsl:if test="@importance='2'">
                    background: url(<xsl:value-of select="$image-location"/>important.png) no-repeat center left;
                  </xsl:if>
                </xsl:attribute>

                <kopete-i18n>%FROM_METACONTACT_DISPLAYNAME%</kopete-i18n>
              </span>

              <span class="time">
                <xsl:attribute name="style">
                  position: relative;
                  background:
                    <xsl:if test="@direction='0'">#c9d9f0</xsl:if>
                    <xsl:if test="@direction='1'">#e1e1e1</xsl:if>
                    url(<xsl:value-of select="$image-location"/>clock.png) no-repeat center right;
                  text-align: right; font-size: 10px; font-weight: bold;
                  padding-right: 20px;
                  padding-left: 5px;
                  float: right;
                  z-index: 1;

                  <xsl:if test="@direction='0'">color: #567199;</xsl:if>
                  <xsl:if test="@direction='1'">color: #707070;</xsl:if>
                </xsl:attribute>

                <xsl:value-of select="@time"/>
              </span>
            </div>
          </div>

          <!-- Contents of the message  - - - - - - - - - - - - - - - - - - -->

          <div class="message_body">
            <xsl:attribute name="style">
              padding-bottom: 7px;

              <xsl:if test="@direction='0'">
                background: #ffffff url(<xsl:value-of select="$image-location"/>corner-bl.png) no-repeat bottom left;
              </xsl:if>
              <xsl:if test="@direction='1'">
                background: #ffffff url(<xsl:value-of select="$image-location"/>corner-br.png) no-repeat bottom right;
              </xsl:if>
            </xsl:attribute>

            <xsl:attribute name="dir">
              <xsl:value-of select="body/@dir"/>
            </xsl:attribute>

            <div>
              <xsl:attribute name="style">
                padding: 5px;
                overflow: auto;

                <xsl:if test="@direction='0'">
                  background: #f5f6fa;
                  border-bottom: 2px solid #c9d9f0;
                </xsl:if>
                <xsl:if test="@direction='1'">
                  background: #f9f9f9;
                  border-bottom: 2px solid #e1e1e1;
                </xsl:if>

                <xsl:if test="body/@font">font:<xsl:value-of select="body/@font"/>;</xsl:if>
                <xsl:if test="body/@color">color:<xsl:value-of select="body/@color"/>;</xsl:if>
                <xsl:if test="body/@bgcolor">background-color:<xsl:value-of select="body/@bgcolor"/>;</xsl:if>

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

              <xsl:if test="not($next_author = $current_author)">
                <xsl:call-template name="render_messages">
                  <xsl:with-param name="messages" select="$messages"/>
                  <xsl:with-param name="position" select="$position"/>
                  <xsl:with-param name="author" select="$current_author"/>
                  <xsl:with-param name="arrow" select="''"/>
                </xsl:call-template>
              </xsl:if>

              <xsl:if test="$next_author = $current_author">
                <xsl:call-template name="render_messages">
                  <xsl:with-param name="messages" select="$messages"/>
                  <xsl:with-param name="position" select="$position"/>
                  <xsl:with-param name="author" select="$current_author"/>
                  <xsl:with-param name="arrow" select="concat($image-location,'arrow',@direction,'.png')"/>
                </xsl:call-template>
              </xsl:if>
            </div>
          </div>
        </xsl:if>
      </xsl:if>


      <!-- Action or System messages  - - - - - - - - - - - - - - - - - - - -->

      <xsl:if test="(@direction='2') or (@direction='3')">

        <xsl:attribute name="style">
          padding-left: 10px; padding-right: 10px;
          border-bottom: 1px dotted #c0c0c0;
          border-top: 1px dotted #c0c0c0;
          vertical-align: middle;
          line-height: 20px;
          height: 20px;
          margin: 5px;
          margin-bottom: 10px;
        </xsl:attribute>

        <span class="contents">
          <xsl:attribute name="style">
            position: absolute;

            <!-- System message -->
            <xsl:if test="@direction='2'">
              background: url(<xsl:value-of select="$image-location"/>system.png) no-repeat center left;
            </xsl:if>

            <!-- Action message -->
            <xsl:if test="@direction='3'">
              background: url(<xsl:value-of select="$image-location"/>action.png) no-repeat center left;
            </xsl:if>

            text-align: left; font-size: 10px; font-weight: bold; color: #808080;
            padding-right: 20px;
            padding-left: 20px;
            overflow: hidden;
            height: 20px;
            float: left;
          </xsl:attribute>

          <xsl:if test="@direction='3'">
            <kopete-i18n>%FROM_METACONTACT_DISPLAYNAME%</kopete-i18n><xsl:text> </xsl:text>
          </xsl:if>

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
      </xsl:if>
    </div>
  </xsl:template>




  <!-- Other messages rendering ============================================-->

  <xsl:template name="render_messages">
    <xsl:param name="messages"/>
    <xsl:param name="position"/>
    <xsl:param name="author"/>
    <xsl:param name="arrow"/>

    <xsl:variable name="current" select="$messages[$position]"/>
    <xsl:variable name="current_author" select="$current/from/contact/@contactId"/>

    <xsl:if test="$current_author = $author">

      <xsl:for-each select="$current">
        <img src="{$arrow}" style="vertical-align: baseline;"/>
        <xsl:value-of disable-output-escaping="yes" select="body"/>
      </xsl:for-each>
      <br/>

      <xsl:call-template name="render_messages">
        <xsl:with-param name="messages" select="$messages"/>
        <xsl:with-param name="position" select="$position + 1"/>
        <xsl:with-param name="author" select="$author"/>
        <xsl:with-param name="arrow" select="$arrow"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>