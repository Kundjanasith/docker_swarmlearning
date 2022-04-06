# Federated Learning Docker on RPI Cluster


> Reference
```bibtex
@article{beutel2020flower,
  title={Flower: A Friendly Federated Learning Research Framework},
  author={Beutel, Daniel J and Topal, Taner and Mathur, Akhil and Qiu, Xinchi and Parcollet, Titouan and Lane, Nicholas D},
  journal={arXiv preprint arXiv:2007.14390},
  year={2020}
}
```

## Configuration

### Model
The deault model is MobileNet
- Modify the global model at line 225 of src/server/server.py
- Modify the local model at line 17 of src/client.py

## Dataset
The default datasets is CIFAR10
- Modify the dataset at line 19 of src/client.py
The default dataset distribution is randomly picking up
- Modify dataset distribution at sampling_data() method of src/client.py

## Federated Learning algorithm
The default federated learning algorithm is FedAvg
- Modify the default federated learning algorithm at line 63 of src/server/server.py

## 
## SERVER

> BUILD
```
sudo docker build -t server -f Dockerfile.server .
```
> RUN
```
sudo docker run -d -p 19191:19191 -v global_models:/global_models kundjanasith/pik8ke_fl:server
```

## CLIENT

> BUILD
```
sudo docker build -t client -f Dockerfile.client .
```
> RUN
```
sudo docker run -d -e server=<server_ip> -e client=<client_ip> -v local_models:/local_models kundjanasith/pik8ke_fl:client
```