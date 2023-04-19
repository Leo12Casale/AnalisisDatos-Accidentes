import pandas as pd
import matplotlib.pyplot as plt
import os

ruta_proyecto = os.path.dirname(__file__)
ruta_datos_csv = os.path.join(ruta_proyecto, 'archivo.csv')

df = pd.read_csv(ruta_datos_csv)
pd.DataFrame(df, columns=['ID','Severity','Start_Time','End_Time','Start_Lat','Start_Lng','End_Lat','End_Lng','Distance(mi)','Description','Number','Street','Side','City','County','State','Zipcode','Country','Timezone','Airport_Code','Weather_Timestamp','Temperature(F)','Wind_Chill(F)','Humidity(%)','Pressure(in)','Visibility(mi)','Wind_Direction','Wind_Speed(mph)','Precipitation(in)','Weather_Condition','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight'])
columns=['ID','Severity','Start_Time','End_Time','Start_Lat','Start_Lng','End_Lat','End_Lng','Distance(mi)','Description','Number','Street','Side','City','County','State','Zipcode','Country','Timezone','Airport_Code','Weather_Timestamp','Temperature(F)','Wind_Chill(F)','Humidity(%)','Pressure(in)','Visibility(mi)','Wind_Direction','Wind_Speed(mph)','Precipitation(in)','Weather_Condition','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight']

#Para graficar ATRIBUTOS
# Calcular la frecuencia de cada categoría en la columna "Severity"
columna="Severity"
freq = df[columna].value_counts()
# Crear un gráfico torta de la frecuencia de cada categoría
freq.plot(kind="pie")
# Agregar etiquetas al gráfico
plt.title("Distribución de " + columna)
plt.show()

#Para graficar INDICADORES
#Establezco los límites del histograma
columna="Visibility(mi)"
valor_min = df[columna].min()
valor_max = df[columna].max()
num_intervalos = 10
amplitud_intervalo = (valor_max - valor_min) / num_intervalos
df[columna].plot.hist(bins=num_intervalos, range=(valor_min, valor_max))
plt.xticks([valor_min + i * amplitud_intervalo for i in range(num_intervalos + 1)])
plt.show()

#df2=df[['Severity']]
#print(df2)
#df2.to_csv('C:\\Users\\leoca\\OneDrive - frc.utn.edu.ar\\Facultad\\5° año\\CDD - Ciencia de Datos\\TPI\\nuevo.csv')