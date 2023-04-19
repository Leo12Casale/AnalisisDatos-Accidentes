import pandas as pd
import matplotlib.pyplot as plt
import time

df= pd.read_csv('C:\\Users\\leoca\\OneDrive - frc.utn.edu.ar\\Facultad\\5° año\\CDD - Ciencia de Datos\\TPI\\archivo.csv')
pd.DataFrame(df, columns=['ID','Severity','Start_Time','End_Time','Start_Lat','Start_Lng','End_Lat','End_Lng','Distance(mi)','Description','Number','Street','Side','City','County','State','Zipcode','Country','Timezone','Airport_Code','Weather_Timestamp','Temperature(F)','Wind_Chill(F)','Humidity(%)','Pressure(in)','Visibility(mi)','Wind_Direction','Wind_Speed(mph)','Precipitation(in)','Weather_Condition','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight'])
columns=['ID','Severity','Start_Time','End_Time','Start_Lat','Start_Lng','End_Lat','End_Lng','Distance(mi)','Description','Number','Street','Side','City','County','State','Zipcode','Country','Timezone','Airport_Code','Weather_Timestamp','Temperature(F)','Wind_Chill(F)','Humidity(%)','Pressure(in)','Visibility(mi)','Wind_Direction','Wind_Speed(mph)','Precipitation(in)','Weather_Condition','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight']

#Para graficar ATRIBUTOS
# Calcular la frecuencia de cada categoría en la columna "Severity"
freq = df["Severity"].value_counts()
# Crear un gráfico torta de la frecuencia de cada categoría
freq.plot(kind="pie")
# Agregar etiquetas al gráfico
plt.title("Distribución de Severidad")
plt.show()

#Para graficar INDICADORES
#Establezco los límites del histograma
bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Crear un histograma con los bins personalizados
freq, bins, patches = plt.hist(df["Visibility(mi)"], bins=bins)
# Agregar etiquetas al gráfico
plt.title("Distribución de Visibilidad")
plt.xlabel("Visibilidad(mi)")
plt.ylabel("Frecuencia")
plt.show()

#df2=df[['Severity']]
#print(df2)
#df2.to_csv('C:\\Users\\leoca\\OneDrive - frc.utn.edu.ar\\Facultad\\5° año\\CDD - Ciencia de Datos\\TPI\\nuevo.csv')