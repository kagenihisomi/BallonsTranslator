from .base import *

@register_translator('Remove Text')
class RemoveTextTranslator(BaseTranslator):

    concate_text = False
    params: Dict = {
    }

    def _setup_translator(self):
        pass

    def _translate(self, src_list: List[str]) -> List[str]:
        
        text = ["" for i in src_list]
        
        return text
    
    def updateParam(self, param_key: str, param_content):
        super().updateParam(param_key, param_content)
        if param_key == 'device':
            if hasattr(self, 'translator'):
                delattr(self, 'translator')

    @property
    def supported_tgt_list(self) -> List[str]:
        return list(LANGMAP_GLOBAL.keys())

    @property
    def supported_src_list(self) -> List[str]:
        return list(LANGMAP_GLOBAL.keys())