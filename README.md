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

## SERVER

> BUILD
```
sudo docker build -t server -f Dockerfile.server .
```
> RUN
```
sudo docker run -d -p 19191:19191 kundjanasith/pik8k3_fl:server
```

## CLIENT

> BUILD
```
sudo docker build -t client -f Dockerfile.client .
```
> RUN
```
sudo docker run -d -e server=<server_ip> -e client=<client_ip> kundjanasith/pik8k3_fl:client
```