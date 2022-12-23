import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from transformers import pipeline
sci_model = pipeline(model="model-attribution-challenge/xlnet-base-cased")

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    #Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        #Add code here
        response = sci_model(text_inputs=request.text)
        #print(response)
        response = response[0][0]['generated_text'][0:200]
        output.append(response)
        #print(response)
    print(output)

    return SimpleText(dict(text=output))
