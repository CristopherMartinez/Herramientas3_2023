import urllib.request
import json
import os
import ssl
import streamlit as st
import pandas as pd
import json

def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

st.title("Formulario para otorgar credito")

#Leer el archivo CSV
datos = pd.read_csv("Herramientas3_2023_banco.csv.csv")
columns = datos.keys()
# Eliminar filas con valores faltantes
datos.dropna(inplace=True)

#lista de elementos de cada columna
listaTrabajos = list(datos["job"].drop_duplicates())
listaCasado = list(datos["marital"].drop_duplicates())
listaEducacion = list(datos["education"].drop_duplicates())
listaDefault  = list(datos["default"].drop_duplicates())
listaHousing = list(datos["housing"].drop_duplicates())
listaloan = list(datos["loan"].drop_duplicates())
listaContacto = list(datos["contact"].drop_duplicates())
listaMes = list(datos["month"].drop_duplicates())
diaWeekList = list(datos["day_of_week"].drop_duplicates())
poutcomeList = list(datos["poutcome"].drop_duplicates())

#Visualizamos las columnas
print(datos.keys())

#obtenemos los datos de cada columna y los ordenamos, despues convertimos a lista y almacenamos
ranEdad = datos[columns[0]].sort_values().tolist()
ranDur = datos[columns[10]].sort_values().tolist()
ranCompania = datos[columns[11]].sort_values().tolist()
ranpdays = datos[columns[12]].sort_values().tolist()
ranprevious = datos[columns[13]].sort_values().tolist()
ranempvarrate = datos[columns[15]].sort_values().tolist()
ranconspriceidx = datos[columns[16]].sort_values().tolist()
ranconsconfidx  = datos[columns[17]].sort_values().tolist()
raneuribor3m = datos[columns[18]].sort_values().tolist()

#Definimos funcion para obtener y mostrar rangos
def obtenerRangos(rango):
    print("El rango de Edad esta entre: " + str(ranEdad[0]) + " y " + str(ranEdad[-1]))
    print("El rango de Duracion esta entre: " + str(ranDur[0]) + " y " + str(ranDur[-1]))
    print("El rango de Compania esta entre: " + str(ranCompania[0]) + " y " + str(ranCompania[-1]))
    print("El rango de Pdays esta entre: " + str(ranpdays[0]) + " y " + str(ranpdays[-1]))
    print("El rango de Previous esta entre: " + str(ranprevious[0]) + " y " + str(ranprevious[-1]))
    print("El rango de Empvarrate esta entre: " + str(ranempvarrate[0]) + " y " + str(ranempvarrate[-1]))
    print("El rango de Conspriceidx esta entre: " + str(ranconspriceidx[0]) + " y " + str(ranconspriceidx[-1]))
    print("El rango de Consconfidx esta entre: " + str(ranconsconfidx[0]) + " y " + str(ranconsconfidx[-1]))
    print("El rango de Euribor3m esta entre: " + str(raneuribor3m[0]) + " y " + str(raneuribor3m[-1]))

#LLamamos a funcion para visualizar los rangos
obtenerRangos(ranEdad)

#Asignamos las listas dependiendo del selectbox y agregamos los rangos
edad = st.number_input(columns[0], min_value=17, max_value=98)

trabajo = st.selectbox(columns[1], listaTrabajos)

casado = st.selectbox(columns[2], listaCasado)

educacion = st.selectbox(columns[3], listaEducacion)

default = st.selectbox(columns[4], listaDefault)

casa = st.selectbox(columns[5], listaHousing)

loan = st.selectbox(columns[6], listaloan)

contacto = st.selectbox(columns[7], listaContacto)

mes = st.selectbox(columns[8], listaMes)

diaSemana = st.selectbox(columns[9], diaWeekList)

duracion = st.number_input(columns[10], min_value=0, max_value=4918)

campania = st.number_input(columns[11], min_value=1, max_value=56)

pdays = st.number_input(columns[12], min_value=0, max_value=999)

previous = st.number_input(columns[13], min_value=0, max_value=7)

poutcome =  st.selectbox(columns[14], poutcomeList)

empvarrate = st.number_input(columns[15], min_value=-3.4, max_value=1.4)

conspriceidx = st.number_input(columns[16], min_value=92.201, max_value=94.767)

consconfidx = st.number_input(columns[17], min_value=-50.8, max_value=-26.9)

euribor3m = st.number_input(columns[18], min_value=0.634, max_value=5.045)

nremployed = st.number_input(columns[19], min_value=4936.6, max_value=5228.1)

#Definimos funcion para que muestre mensaje al final si aplica o no al credito
def verificarDatos(res):
    if res == "no":
        st.subheader('No aplicas al credito sigue intentando :disappointed_relieved:')
    else:
        st.subheader('Si aplicas al credito felicidades!! :sunglasses:')
        st.balloons()

data =  {
  "Inputs": {
    "data": [
      {
        "age": edad,
        "job": trabajo,
        "marital": casado,
        "education": educacion,
        "default": default,
        "housing": casa,
        "loan": loan,
        "contact": contacto,
        "month": mes,
        "duration": duracion,
        "campaign": campania,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome,
        "emp.var.rate": empvarrate,
        "cons.price.idx": conspriceidx,
        "cons.conf.idx": consconfidx,
        "euribor3m": euribor3m,
        "nr.employed": nremployed
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}
data.items();
body = str.encode(json.dumps(data))

url = 'https://fca-regression.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = 'AnVcIXbYyV9KbCKmAGmbV2gNhpMAdmXg'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'fca-deploy2' }

req = urllib.request.Request(url, body, headers)

try:

    if st.button('Verificar'):
        response = urllib.request.urlopen(req)
        result = response.read()
        #print(result)
        resultado_str = result.decode('utf-8')
        resultadoDiccio = json.loads(resultado_str)
        resultado = resultadoDiccio["Results"][0]
        resp = str(resultado)
        verificarDatos(resp)

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))




