import json
from flask import Flask
from flask import jsonify
from flask import request    
app = Flask(__name__)

class Patient:
  #Construtor
  def __init__(self):
    self.first_name = first_name
    self.last_name = last_name
    self.oxigenacao = oxigenacao
    self.name = name
    # self.name.append(self.first_name)
    # self.name.append(self.last_name)
    self.name = ''.join((self.first_name," ",self.last_name))

patients = [] # array que vai armazenar os pacientes e seus dados

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Olá!'})

# We're using the new route that allows us to read a date from the URL
@app.route('/pacientes', methods = ['GET'])
def returnAll():
  # data = request.get_data().decode()
  return jsonify({'patients' : patients})
  # return request.headers.get('your-header-name')

@app.route('/pacientes', methods=['POST'])
def addOne():
    new_patient = request.get_json()
    new_patient_data = json.loads(new_patient)
    patients.append(new_patient_data)
    # patients.insert(new_patient)
    return jsonify({'patients' : patients}) 

@app.route('/pacientes', methods=['PUT'])
def editAll():
    # patient_stored = Patient() # aqui serao carregados os dados contidos no array já armazenado no server até agora
    
    new_patient = request.get_json()
    new_patient_data = json.loads(new_patient)
    
    tmp_buffer = []
    tmp_buffer.append(new_patient_data['nome'])
    tmp_buffer.append(new_patient_data['oxigenacao'])
    # print("asidoasidoa")
    print(tmp_buffer)
    # patient_stored.first_name = new_patient_data
    for patient in patients:
      # se o nome do paciente já estiver registrado atualiza seu valor de oxigenação
      if(patient['nome'] == tmp_buffer[0]):
        patient['oxigenacao'] = tmp_buffer[1]
      print ("dentro do put req mas fora do if")
      print(patient)
      print(patients)
    #   if (patie)
    # for patient in patients
    #   if patient
    #     patients[i] = new_patient    
    # ps = request.get_json()
    return jsonify({'patients' : patients})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
