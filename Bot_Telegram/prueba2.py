import telebot
from telebot.types import ReplyKeyboardMarkup #Para crear botones en el teclado
from telebot.types import ForceReply #para citar un mensaje
from telebot.types import ReplyKeyboardRemove # para elinina botones
from pymongo import MongoClient #biblioteca para conexión a mongo

#instanciamos el bot de telegram
bot = telebot.TeleBot('7127293958:AAEbBq2GvVRpD9--NNm3sk6EtbWh2KqjK7E')
#Variable global en la que se almacenaran los datos del usuario
usuarios = {}

#conexion a la base de datos
def get_db():
    try:
        client = MongoClient('mongodb+srv://lupitapb:root@cluster0.3qz2pqw.mongodb.net/ejemplo?retryWrites=true&w=majority&appName=Cluster00')
        database = client['ejemplo']
    except Exception as ex:
        print(f'Error: {ex}')
    return database


#responde al comando /botones
@bot.message_handler(commands=['encuesta'])
def cmd_botones(message):
    """Muestra un mensaje con botones inline (acontuacion del mensaje)."""
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
    markup.add("Masculino", "Femenino")
    msg = bot.send_message(message.chat.id, 'Selecciona tu genero: ', reply_markup=markup)
    bot.register_next_step_handler(msg, pregunta_edad)

def pregunta_edad(message):
    if message.text != "Masculino" and message.text != "Femenino":
        msg = bot.send_message(message.chat.id, 'ERROR: Genero no válido.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_edad)
    else:
        genero = ""
        if message.text == "Masculino":
            genero = "M"
        if message.text == "Femenino":
            genero = "F"
        usuarios[message.chat.id] = {}
        usuarios[message.chat.id]["Genero"] = genero
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "¿Cuántos años tienes?", reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_fumador)

def pregunta_fumador(message):
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "ERROR: Debes indicar tu edad con numeros.\n¿Cuántos años tienes?")
        bot.register_next_step_handler(msg, pregunta_fumador)
    else:
        usuarios[message.chat.id]["Edad"] = int(message.text)
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Se considera una persona que fuma mucho?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_dedos_amarillos)

def pregunta_dedos_amarillos(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_dedos_amarillos)
    else:
        fumador = 0
        if message.text == "Si":
            fumador = 2
        if message.text == "No":
            fumador = 1
        usuarios[message.chat.id]["Fumador"] = fumador
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene los dedos amarillos?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_ansiedad)

def pregunta_ansiedad(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_ansiedad)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Dedos Amarillos"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene ansiedad?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_presion_de_grupo)

def pregunta_presion_de_grupo(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_presion_de_grupo)
    else: 
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Ansiedad"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Siente presión social para realizar malos hábitos?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_cronica)

def pregunta_cronica(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_cronica)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Presion de grupo"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene alguna enfermedad crónica?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_fatiga)

def pregunta_fatiga(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_fatiga)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Enfermedad Cronica"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Siente fatiga?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_alergia)

def pregunta_alergia(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_alergia)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Fatiga"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene alguna alergia?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_sibilancias)
    
def pregunta_sibilancias(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_sibilancias)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Alergia"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Te silba el pecho?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_alcohol)

def pregunta_alcohol(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_alcohol)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Silbilancias"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Toma bebidas alcohólicas?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_tos)

def pregunta_tos(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_tos)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Alcohol"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene tos?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_respirar)

def pregunta_respirar(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_respirar)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Tos"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene problemas para respirar?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_tragar)

def pregunta_tragar(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_tragar)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Dificultad para respirar"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene dificultad para ingerir alimentos?', reply_markup=markup)
        bot.register_next_step_handler(msg, pregunta_pecho)

def pregunta_pecho(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_pecho)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Dificultad para tragar"] = dedos
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder= "Pulsa el boton", resize_keyboard=True)
        markup.add("Si", "No")
        msg = bot.send_message(message.chat.id, '¿Tiene dolor de pecho?', reply_markup=markup)
        bot.register_next_step_handler(msg, mostrar_datos)

def mostrar_datos(message):
    if message.text != "Si" and message.text != "No":
        msg = bot.send_message(message.chat.id, 'ERROR: Respuesta invalida.\nPulsa un boton')
        bot.register_next_step_handler(msg, pregunta_pecho)
    else:
        dedos = 0
        if message.text == "Si":
            dedos = 2
        if message.text == "No":
            dedos = 1
        usuarios[message.chat.id]["Dolor de pecho"] = dedos
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '¡Gracias por contestar la encuesta!', reply_markup=markup)
        resultado = 'Datos introducidos: \n'
        resultado += f'<code>Genero: </code> {usuarios[message.chat.id]["Genero"]}\n'
        resultado += f'<code>Edad: </code> {usuarios[message.chat.id]["Edad"]}\n'
        resultado += f'<code>Fumador: </code> {usuarios[message.chat.id]["Fumador"]}\n'
        resultado += f'<code>Dedos amarillos: </code> {usuarios[message.chat.id]["Dedos Amarillos"]}\n'
        resultado += f'<code>Ansiedad: </code> {usuarios[message.chat.id]["Ansiedad"]}\n'
        resultado += f'<code>Presion de grupo: </code> {usuarios[message.chat.id]["Presion de grupo"]}\n'
        resultado += f'<code>Enfermedad cronica: </code> {usuarios[message.chat.id]["Enfermedad Cronica"]}\n'
        resultado += f'<code>Fatiga: </code> {usuarios[message.chat.id]["Fatiga"]}\n'
        resultado += f'<code>Alergia: </code> {usuarios[message.chat.id]["Alergia"]}\n'
        resultado += f'<code>Silbilancias: </code> {usuarios[message.chat.id]["Silbilancias"]}\n'
        resultado += f'<code>Alcohol: </code> {usuarios[message.chat.id]["Alcohol"]}\n'
        resultado += f'<code>Tos: </code> {usuarios[message.chat.id]["Tos"]}\n'
        resultado += f'<code>Dificualtad para respirar: </code> {usuarios[message.chat.id]["Dificultad para respirar"]}\n'
        resultado += f'<code>Dificultad para tragar: </code> {usuarios[message.chat.id]["Dificultad para tragar"]}\n'
        resultado += f'<code>Dolor de pecho: </code> {usuarios[message.chat.id]["Dolor de pecho"]}\n'
        bot.send_message(message.chat.id, resultado, parse_mode="html")

        #Formato en el cual se enviran los datos a la base de datos
        data = {
            "Sexo": usuarios[message.chat.id]["Genero"],
            "Edad": usuarios[message.chat.id]["Edad"],
            "Fumador": usuarios[message.chat.id]["Fumador"],
            "dedos Amarillos": usuarios[message.chat.id]["Dedos Amarillos"],
            "Ansiedad": usuarios[message.chat.id]["Ansiedad"],
            "presion de grupo": usuarios[message.chat.id]["Presion de grupo"],
            "enfermedad cronica": usuarios[message.chat.id]["Enfermedad Cronica"],
            "fatiga": usuarios[message.chat.id]["Fatiga"],
            "Alergia": usuarios[message.chat.id]["Alergia"],
            "Silbilancias": usuarios[message.chat.id]["Silbilancias"],
            "Consumo Alcohol": usuarios[message.chat.id]["Alcohol"],
            "Tos": usuarios[message.chat.id]["Tos"],
            "Dificultad respirar": usuarios[message.chat.id]["Dificultad para respirar"],
            "Dificultad tragar": usuarios[message.chat.id]["Dificultad para tragar"],
            "Dolor en pecho": usuarios[message.chat.id]["Dolor de pecho"]
        }
        #Llamada a la conexion de la BD
        db = get_db()
        #Inserta los datos
        db.tabla1.insert_one(data)
        #Imprime los datos pero en la linea de comandos
        print(usuarios)
        #Elimina los datos que anteriormente se mostraron de la memoria cache
        del usuarios[message.chat.id]

if __name__ == "__main__":
    print("Bot iniciado")
    bot.infinity_polling()


