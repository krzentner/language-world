
"""


from allennlp.common import Params
import numpy as np
from nltk import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import torch
from torch import nn
from torch.utils.data import DataLoader
from allennlp.modules.text_field_embedders import TextFieldEmbedder, BasicTextFieldEmbedder
from allennlp.modules.token_embedders import Embedding
from allennlp.modules.seq2seq_encoders import Seq2SeqEncoder
from allennlp.nn import InitializerApplicator, RegularizerApplicator
from allennlp.nn.util import get_text_field_mask
from allennlp.data.dataset_readers.dataset_reader import DatasetReader
from allennlp.data.token_indexers.token_indexer import TokenIndexer
from allennlp.data.tokenizers import Token, Tokenizer
from allennlp.data.token_indexers import SingleIdTokenIndexer
from allennlp.data.instance import Instance
from allennlp.common.util import START_SYMBOL, END_SYMBOL
from allennlp.data.tokenizers.pretrained_transformer_tokenizer import PretrainedTransformerTokenizer
from allennlp.data.tokenizers import Tokenizer
from ..data.dataset_readers.language_generation_reader import \
    LanguageGenerationInstance, LanguageGenerationReader
from ..data.tokenizers import \
    PretrainedTransformerTokenizer, \
    RobertaCharTokenizer
from ..modules.seq2seq_encoders.roberta_lm_sequence_encoder import RobertaLMSequenceEncoder

from ..modules.language_generation_heads.language_generation_head import \
    LanguageGenerationHead
from ..modules.language_generation_heads.roberta_lm_head import RobertaLMHead
from ..modules.seq2seq_encoders.roberta_lm_sequence_encoder import RobertaLMSequenceEncoder
from ..modules.token_embedders.roberta_token_embedder import RobertaTokenEmbedder

def test_roberta_language_generation_step_by_step_with_attention_head():
    import torch

    tokenizer = PretrainedTransformerTokenizer("roberta-base")
    words = ["Hello", "world", "!"]
    token_ids = tokenizer.tokens_to_ids(words)
    segments_ids = [0, 0, 0]
    type_ids =