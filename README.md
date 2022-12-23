# Openfabric Test
#### NLP chatbot for answering questions about science by [Ritik Bompilwar](https://ritik.app/).

## ✯ Instructions

Please run the following command to get the system running.

1. ` git clone https://github.com/RITIK-12/openfabrictest.git`


2. `pip install -r requirements.txt`


3. ` ./start.sh`
  
## ✯ Model
The XLNet was introduced in the paper [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) by Yang et al. The model is pre-trained on [wikipedia](https://huggingface.co/datasets/wikipedia) and [bookcorpus](https://huggingface.co/datasets/bookcorpus) datasets. Here, the model is used in the inference mode only and integrated into the openfabric pipeline.

<img width="1064" alt="Screenshot 2022-12-23 at 10 01 18 PM" src="https://user-images.githubusercontent.com/54806252/209368228-5e623c29-6176-44d2-b7aa-61ce2d2a7fa5.png">



The [XLNet model](https://huggingface.co/model-attribution-challenge/xlnet-base-cased) is used for question answering via huggingface pipeline. XLNet is a new unsupervised language representation learning method based on a novel generalized permutation language modeling objective. It employs Transformer-XL as the backbone model, exhibiting excellent performance for language tasks involving long context. XLNet achieves state-of-the-art (SOTA) results on various downstream language tasks including question answering, natural language inference, sentiment analysis, and document ranking.


## ✯ Implementation
![openfabric](https://user-images.githubusercontent.com/54806252/209370507-0bf163e7-a992-4d01-8c89-2d90c2e47f30.gif)
