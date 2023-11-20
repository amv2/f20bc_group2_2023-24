from BIC_CW.Regular import regular_run

regular_run(data_path="/home/amv2/Codespace/Uni/personal-coursework/F21BC/data/data_banknote_authentication.csv",
            nb_layers=10,
            nb_nodes=24,
            list_func="relu",
            loss_func="bce",
            swarmsize=55,
            alpha=0.9,
            beta=0.8,
            gamma=0.7,
            delta=0.6,
            jump_size=0.1,
            max_iter=70,
            num_informants=5,
            pso_type="type3")
