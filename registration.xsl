<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
   <html lang="en">
       <head>
            <meta charset="UTF-8"/>
            <title>Cars registering</title>
            <style type="text/css">
                body {
                    background-color: linen;
                    font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
                }

                h1 {
                    color: grey;
                    font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
                }
                .center {
                    text-align: center;
                    border: 3px solid black;
                }
               .add-row {
                   color: #006b1b;
                   font-weight: bold;
                   font-style: normal;
               }
               .delete-row {
                   color: #a41515;
                   font-weight: bold;
                   font-style: normal;
               }
               input {
                   width: 300px;
               }
               label {
                   padding: 12px 12px 12px 0;
                   display: inline-block;
               }
            </style>
       </head>
       <body>
           <div class="center">
                <h1> Cars Race registering page </h1>
                <div>
                    <form method="post" action="">
                        <fieldset>
                            <div>
                                <h2> Identify yourself </h2>
                                <label>First name </label> <input value="{registration/user/first_name}" name="first_name" id="first_name"
                                binding="registration/user/first_name" ftXPath="registration/user/first_name" readonly="True"/>
                                <br>
                                <label>Second name </label> <input value="{registration/user/second_name}" name="second_name" id="second_name"
                                binding="registration/user/second_name" ftXPath="registration/user/second_name" readonly="True"/>
                                </br>
                                <label>Email </label> <input value="{registration/user/email}" name="email" id="email"
                                binding="registration/user/email" ftXPath="registration/user/email" readonly="True"/>
                                <br>
                                <label>ID_number </label> <input value="{registration/user/ID_number}" name="ID_number" id="ID_number"
                                binding="registration/user/ID_number" ftXPath="registration/user/ID_number" readonly="True"/>
                                </br>

                                <xsl:for-each select="registration/car_list/car">
                                    <h2> Car details </h2>
                                     <label>Car brand </label> <input value="{car_brand}" name="car_brand" id="car_brand"
                                    binding="registration/car_list/car/car_brand" ftXPath="registration/car_list/car/car_brand" readonly="True"/>
                                    <br>
                                     <label>Car type </label> <input value="{car_type}" name="car_type" id="car_type"
                                    binding="registration/car_list/car/car_type" ftXPath="registration/car_list/car/car_type" readonly="True"/>
                                    </br>
                                     <label>SPZ </label> <input value="{spz}" name="spz" id="spz"
                                    binding="registration/car_list/car/spz" ftXPath="registration/car_list/car/spz" readonly="True"/>
                                    <br>
                                    <label>Registration date </label> <input value="{registration_date}" name="registration_date" id="registration_date"
                                    binding="registration/car_list/car/registration_date" ftXPath="registration/car_list/car/registration_date" readonly="True"/>
                                    </br>
                                    <label>Car VIN </label> <input value="{vin}" name="vin" id="vin"
                                    binding="registration/car_list/car/vin" ftXPath="registration/car_list/car/vin" readonly="True"/>
			                    </xsl:for-each>
                            </div>
                        </fieldset>
                    </form>
                </div>
           </div>
       </body>
   </html>
</xsl:template>

</xsl:stylesheet>