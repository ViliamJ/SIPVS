<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:fo="http://www.w3.org/1999/XSL/Format">

	<xsl:template match="/">
		<html>
		<body>
		<table border="1">
			<tr>
				<th>first name</th>
				<th>second name</th>
				<th>email</th>
				<th>ID_number</th>
			</tr>
			<xsl:for-each select="//registration">
			   <xsl:apply-templates select="user"/>
			 </xsl:for-each>
		</table>

		 <table border="1">
			<tr>
				<th>car brand</th>
				<th>car type</th>
				<th>spz</th>
				<th>registration date</th>
				<th>vin</th>
			</tr>
			 <xsl:for-each select="//registration/car_list">
			   <xsl:apply-templates select="car"/>
			 </xsl:for-each>
		 </table>
		</body>
		</html>
    </xsl:template>

	<xsl:template match="user">
		<tr>
			<td>
				<xsl:value-of select="first_name"/>
			</td>
			<td>
				<xsl:value-of select="second_name"/>
			</td>
			<td>
				<xsl:value-of select="email"/>
			</td>
			<td>
				<xsl:value-of select="ID_number"/>
			</td>
		</tr>
	</xsl:template>

	<xsl:template match="car">
		<tr>
			<td>
				<xsl:value-of select="car_brand"/>
			</td>
			<td>
				<xsl:value-of select="car_type"/>
			</td>
			<td>
				<xsl:value-of select="spz"/>
			</td>
			<td>
				<xsl:value-of select="registration_date"/>
			</td>
			<td>
				<xsl:value-of select="vin"/>
			</td>
		</tr>
	</xsl:template>

</xsl:stylesheet>
