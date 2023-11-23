from flask import Flask, request, jsonify
import json

from BIC_CW.Regular import regular_run

# initialize metrics to send back to the frontend
accuracy = "0.0"
fitness = "0.0"
loss = "0.0"
time = "0.0"


def extract_int_float_data(int_dict, float_dict):
    nb_layers = int_dict['intValue1']
    nb_nodes = int_dict['intValue2']
    swarmsize = int_dict['intValue3']
    alpha = float_dict['floatValue1']
    beta = float_dict['floatValue2']
    gamma = float_dict['floatValue3']
    delta = float_dict['floatValue4']
    jump_size = float_dict['floatValue5']
    max_iter = int_dict['intValue4']
    num_informants = int_dict['intValue5']
    list_func = int_dict['intValue6']
    loss_func = int_dict['intValue7']

    accuracy, fitness, loss, time = regular_run(nb_layers=nb_layers,
                                                nb_nodes=nb_nodes,
                                                list_func=list_func,
                                                loss_func=loss_func,
                                                swarmsize=swarmsize,
                                                alpha=alpha,
                                                beta=beta,
                                                gamma=gamma,
                                                delta=delta,
                                                jump_size=jump_size,
                                                max_iter=max_iter,
                                                num_informants=num_informants)

    data = [accuracy, fitness, loss, time]
    return data


app = Flask(__name__)


@app.route('/receive_data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        # load the json data
        received_data = request.get_data()
        decoded_data = received_data.decode('utf-8')
        parsed_data = json.loads(decoded_data)

        int_dict = {}
        float_dict = {}

        # extract the int and float data and add it to their respective dicts
        for key, value in parsed_data.items():
            if key.startswith('intValue'):
                int_dict[key] = value
            elif key.startswith('floatValue'):
                float_dict[key] = value

        data = extract_int_float_data(int_dict=int_dict, float_dict=float_dict)

        # convert the data to string and send it back to the front end
        accuracy = str(data[0])
        fitness = str(data[1])
        loss = str(data[2])
        time = str(data[3])

        return jsonify([accuracy, fitness, loss, time])


if __name__ == '__main__':
    app.run(debug=True)
