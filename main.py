import json
import re

# json mockado - é possivel fazer uma chamada para endpoint do flask

j = '{ "CALCULO_CCF_CEA": 0,     "CALCULO_CCF_KREG": 0,     "CALCULO_CEA_RAROC": 3948681.0,     ' \
    '"CALCULO_CRIACAO_VALOR": -225788.0,     "CALCULO_CUSTOSADM_RAROC": 0.0,     ' \
    '"CALCULO_CUSTO_CAPITAL": 524670.0,     ' \
    '"CALCULO_EAD_CEA_MEDIA": 52367320,     "CALCULO_EAD_KREG_MEDIA": 52367320,     ' \
    '"CALCULO_GIROPROPRIO_RAROC": 439545,     "CALCULO_IR_RAROC": 186183.0,     ' \
    '"CALCULO_JCP_RAROC": 71325.0,     "CALCULO_MFB_RAROC": 0,     "CALCULO_PERC_CEA_RAROC": "7,5",     ' \
    '"CALCULO_PERC_UTI": "Em breve",     "CALCULO_PERDA_RAROC": 5367,     "CALCULO_PZO_TOTAL": "365 Dias",     ' \
    '"CALCULO_RAROC_COMBINADO": "7,8",     "CALCULO_RAROC_GRUPO": "0,0",     "CALCULO_RAROC_OPERACAO": "7,8",     ' \
    '"CALCULO_RECEITAS_RAROC": 0.0,     "CALCULO_RESULTADO_ANTES_IR_RAROC": 413739.0,     "CALCULO_RES_META": 0,     ' \
    '"CALCULO_RGO_RAROC": 298882.0,     "CALCULO_ROE_OPERACAO": "",     "CALCULO_SPREAD_RAROC": 0.0,     ' \
    '"CALCULO_SPREAD_ROE": 0.0,     "CALCULO_TRIBUTARIAS_RAROC": 20439,     "DELTA_CV": 225788.49920403823,     ' \
    '"DELTA_POOL": 152695.23022440582,     "HURDLE": 0.14000000000000007,     "PGTO_ATIVOS": 0,     ' \
    '"PGTO_ATIVOS_PAR": 0.0,     "PGTO_ATIVOS_VP": 0.0,     "PGTO_PASSIVOS": 0,     "PGTO_PASSIVOS_PAR": 0.0,     ' \
    '"PGTO_PASSIVOS_VP": 0.0,     "RESULTADO_VENDA": 0.0,     "RESULTADO_VENDA_LIQ": 0.0,     "VL_BOF": 0,     ' \
    '"calculo_custo_adm_roe": 0.0,     "calculo_giroproprio_roe": 696296.0,     "calculo_ir_roe": 296348.0,     ' \
    '"calculo_jcp_roe": 113510.0,     "calculo_kreg_roe": 6284078,     "calculo_mfb_roe": 0,     ' \
    '"calculo_perc_kreg_roe": "12,0",     "calculo_perda_roe": 5,     "calculo_receitas_roe": 0.0,     ' \
    '"calculo_resultado_antes_ir_roe": 658551.0,     "calculo_rgo_roe": 475713.0,     ' \
    '"calculo_tributarias_roe": 32378.0 }'

# Convert JSON to String


json_load = (json.loads(j))
campo_calculo = json_load['calculo_perda_roe']

# A função esta referente ao 1 campo do json de exemplo ( pode ser medido  +1 de 1 campo )


def regua_cliente (campo_calculo):
    if 0 < campo_calculo < 1341:
        output_json = {"visao_cliente": "Excelente"}
        b = json.dumps(output_json)

    if 1342 < campo_calculo < 2682:
        output_json = {"visao_cliente": "Medio"}
        b = json.dumps(output_json)

    if 2683 < campo_calculo < 4023:
        output_json =  {"visao_cliente": "Insufuciente"}
        b = json.dumps(output_json)

    if campo_calculo > 4023:
        output_json = {"visao_cliente": "Ruim"}
        b = json.dumps(output_json)

    return b


print(regua_cliente(campo_calculo))




