# Federated Learning Docker on RPI Cluster


Ref:
```bibtex
@article{beutel2020flower,
  title={Flower: A Friendly Federated Learning Research Framework},
  author={Beutel, Daniel J and Topal, Taner and Mathur, Akhil and Qiu, Xinchi and Parcollet, Titouan and Lane, Nicholas D},
  journal={arXiv preprint arXiv:2007.14390},
  year={2020}
}
```

Command:
```
docker run -p 19191:19191 \
 -e server=<server_ip> \
 -e client=<client_ip> \
 -e server_status=<True,False> \ #Default False
 -e client_status=<True,False> \ #Default False
 -d <image_id>
```