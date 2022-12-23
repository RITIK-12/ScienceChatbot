# Openfaric Test
#### NLP chatbot for answering questions about science by [Ritik Bompilwar](https://ritik.app/)

### Instructions
1. ` git clone https://github.com/RITIK-12/openfabrictest.git`


2. `pip install -r requirements.txt`


3. ` ./start.sh`
  
### Model
<img width="1095" alt="Screenshot 2022-12-23 at 9 58 24 PM" src="https://user-images.githubusercontent.com/54806252/209367920-0a102aeb-3ad5-42d1-a453-912f1b55d7f1.png">

The [XLNet model](https://huggingface.co/model-attribution-challenge/xlnet-base-cased) is used for question answering via huggingface pipeline. XLNet is a new unsupervised language representation learning method based on a novel generalized permutation language modeling objective. It employs Transformer-XL as the backbone model, exhibiting excellent performance for language tasks involving long context. XLNet achieves state-of-the-art (SOTA) results on various downstream language tasks including question answering, natural language inference, sentiment analysis, and document ranking.

The XLNet was introduced in the paper [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) by Yang et al. The model is pre-trained on [wikipedia](https://huggingface.co/datasets/wikipedia) and [bookcorpus](https://huggingface.co/datasets/bookcorpus) datasets. Here, the model is used in the inference mode only and integrated into the openfabric pipeline.

### Implementation


