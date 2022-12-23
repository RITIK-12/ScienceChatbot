# Openfaric Test
#### NLP chatbot for answering questions about science by [Ritik Bompilwar](https://ritik.app/)

### Instructions
1. ` git clone https://github.com/RITIK-12/openfabrictest.git`


2. `pip install -r requirements.txt`


3. ` ./start.sh`
  
### Model
![image](https://user-images.githubusercontent.com/54806252/209368115-95eb6734-66b4-4a63-96e7-494a036a46d5.png)


The [XLNet model](https://huggingface.co/model-attribution-challenge/xlnet-base-cased) is used for question answering via huggingface pipeline. XLNet is a new unsupervised language representation learning method based on a novel generalized permutation language modeling objective. It employs Transformer-XL as the backbone model, exhibiting excellent performance for language tasks involving long context. XLNet achieves state-of-the-art (SOTA) results on various downstream language tasks including question answering, natural language inference, sentiment analysis, and document ranking.

The XLNet was introduced in the paper [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) by Yang et al. The model is pre-trained on [wikipedia](https://huggingface.co/datasets/wikipedia) and [bookcorpus](https://huggingface.co/datasets/bookcorpus) datasets. Here, the model is used in the inference mode only and integrated into the openfabric pipeline.

### Implementation


