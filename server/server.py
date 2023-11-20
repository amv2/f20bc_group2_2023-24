from flask import Flask, request, jsonify
import json

from BIC_CW.Regular import regular_run

accuracy = "0.0"
fitness = "0.0"
loss = "0.0"


def extract_int_float_data(int_dict, float_dict):
    nb_layers = int_dict['intValue1']
    nb_nodes = int_dict['intValue2']
    list_func = "relu"
    loss_func = "bce"
    swarmsize = int_dict['intValue3']
    alpha = float_dict['floatValue1']
    beta = float_dict['floatValue2']
    gamma = float_dict['floatValue3']
    delta = float_dict['floatValue4']
    jump_size = float_dict['floatValue5']
    max_iter = int_dict['intValue4']
    num_informants = int_dict['intValue5']
    pso_type = "type3"

    accuracy, fitness, loss = regular_run(data_path="/home/amv2/Codespace/Uni/personal-coursework/F21BC/data/data_banknote_authentication.csv",
                                          nb_layers=nb_layers,
                                          nb_nodes=nb_nodes,
                                          list_func="relu",
                                          loss_func="bce",
                                          swarmsize=swarmsize,
                                          alpha=alpha,
                                          beta=beta,
                                          gamma=gamma,
                                          delta=delta,
                                          jump_size=jump_size,
                                          max_iter=max_iter,
                                          num_informants=num_informants,
                                          pso_type="type3")

    data = [accuracy, fitness, loss]
    return data


app = Flask(__name__)


@app.route('/receive_data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        received_data = request.get_data()
        decoded_data = received_data.decode('utf-8')
        parsed_data = json.loads(decoded_data)

        int_dict = {}
        float_dict = {}

        for key, value in parsed_data.items():
            if key.startswith('intValue'):
                int_dict[key] = value
            elif key.startswith('floatValue'):
                float_dict[key] = value

        print("Integer dictionary:", int_dict)
        print("Float dictionary:", float_dict)

        data = extract_int_float_data(int_dict=int_dict, float_dict=float_dict)

        accuracy = str(data[0])
        fitness = str(data[1])
        loss = str(data[2])

        # Perform any necessary processing or store the data in variables/database

        return jsonify([accuracy, fitness, loss])


@app.route('/send_data', methods=['POST'])
def send_data():
    # return jsonify([accuracy, fitness, loss])
    data_to_send = request.json
    sent_data = {'result': data_to_send}
    return jsonify(sent_data)


if __name__ == '__main__':
    app.run(debug=True)
