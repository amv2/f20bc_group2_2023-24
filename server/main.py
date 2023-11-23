from BIC_CW.Regular import regular_run

regular_run(nb_layers=3,
            nb_nodes=10,
            list_func=1,
            loss_func=2,
            swarmsize=100,
            alpha=0.9,
            beta=0.8,
            gamma=0.7,
            delta=0.6,
            jump_size=0.1,
            max_iter=100,
            num_informants=3)
