#!usr/bin/python3
import requests
from time import sleep
import os
#cores
vd='\033[1;32m'         
am='\033[1;33m'  
vm='\033[31m'
az='\033[1;31m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'   
mg='\033[1;35m1' 
def ip():  
    n1 = str(input(f'{vm}--={f}{az}[CONSULTA IP]{f}\n\n- {az}[{f}{lz}01{f}{az}]{f} {ng}ipgeolocation{f}\n- {az}[{f}{lz}02{f}{az}]{f} {ng}ip{f}\n- {az}[{f}{lz}03{f}{az}]{f} {ng}ipfind{f}  \n- {am}+=>{f} '))         
    if n1=='1' or n1=='01':
        ip1=input(f'{vm}--=={f}{az}[fonte IPGEOLOCATION]{f} \n{vm}--=={f}{az}[ ip ]{f} {am}+=>{f} ')
        url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}".format(ip1)
        res = requests.get(url1)
        req=res.json()
        br="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA cyberPESTE \n[+] by: CYBERpeste{}{} \n-=[ip]:{}\n-=[código do continente]:{}\n-=[nome do continente]:{}\n-=[código do país 2]:{}\n-=[código do país 3]:{}\n-=[nome do país]:{}\n-=[capital do país]:{}\n-=[prov do estado]:{}\n-=[distrito]:{}\n-=[cidade]:{}\n-=[CEP]:{}\n-=[latitude]:{}\n-=[longitude]:{}\n-=[is_eu]:{}\n-=[código de chamada]:{}\n-=[país tld]:{}\n-=[languages]:{}\n-=[bandeira do país]:{}\n-=[ geoname_id ]:{}\n-=[ isp ]:{}\n-=[continente]:{}\n-=[organização]:{}\n-=[moeda]:{}\n-=[fuso horário]:{}\n\033[m".format(ng,f,vd,req['ip'],req['continent_code'],req['continent_name'],req['country_code2'],req['country_code3'],req['country_name'],req['country_capital'],req['state_prov'],req['district'],req['city'],req['zipcode'],req['latitude'],req['longitude'],req['is_eu'],req['calling_code'],req['country_tld'],req['languages'],req['country_flag'],req['geoname_id'],req['isp'],req['connection_type'],req['organization'],req['currency'],req['time_zone'])
        print(br)


    elif n1=='2' or n1=='02':            
        ip2=input(f'{vm}--=={f}{az}[fonte IP ]{f} \n{vm}--=={f}{az}[ ip ]{f} {am}+=>{f} ')      
        url2='http://ip-api.com/json/{}'.format(ip2)
        res2=requests.get(url2);req1=res2.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        br2="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA cyberPESTE \n[+] by: cyberPESTE{}\n {}-=[status]:{}\n -=[país]:{}\n -=[código do país]:{}\n -=[região]:{}\n -=[nome da região]:{}\n -=[cidade]:{}\n -=[zip]:{}\n -=[lat]:{}\n -=[lon]:{}\n -=[fuso horário]:{}\n -=[isp]:{}\n -=[org]:{}\n -=[as]:{} {}\033[m".format(ng,f,vd,req1['status'],req1['country'],req1['countryCode'],req1['region'],req1['regionName'],req1['city'],req1['zip'],req1['lat'],req1['lon'],req1['timezone'],req1['isp'],req1['org'],req1['as'],req1['query'],f)       
        print(br2)
        exit()
    elif n1=='3' or n1=='03':     
        ip3=input(f'{vm}--=={f}{az}[fonte IPFIND ]{f} \n{vm}--=={f}{az}[ ip ]{f} {am}+=>{f} ')
        url3='https://api.ipfind.com/?ip={}&auth=22e75f18-7853-4227-ac49-3a8a72893210'.format(ip3)
        res3=requests.get(url3);req3=res3.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        br3='\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA cyberPESTE \n[+] by: cyberPESTE{}\n{}-=[ip_address]:{}\n-=[country]:{}\n-=[country code]:{}\n-=[continent]:{}\n-=[continente codigo]:{}\n-=[city]:{}\n-=[condado]:{}\n-=[região]:{}\n-=[código da região]:{}\n-=[fuso horário]:{}\n-=[proprietário]:{}\n-=[longitude]:{}\n-=[latitude]:{}\n-=[moeda]:{}\n-=[línguas]:{}\n{}'.format(ng,f,vd,req3['ip_address'],req3['country'],req3['country_code'],req3['continent'],req3['continent_code'],req3['city'],req3['county'],req3['region'],req3['region_code'],req3['timezone'],req3['owner'],req3['longitude'],req3['latitude'],req3['currency'],req3['languages'],f)
        print(br3)
def cep():    
    n1 = str(input(f'{vm}--={f}{az}[CONSULTA CEP]{f}\n\n- {az}[{f}{lz}1{f}{az}]{f} {ng}postmon{f}\n- {az}[{f}{lz}2{f}{az}]{f} {ng}viacep{f}\n- {az}[{f}{lz}3{f}{az}]{f} {ng}apicep{f}  \n- {am}+=>{f} '))
    if n1=='1' or n1=='01':
        cep1=input(f'{vm}--=={f}{az}[fonte POSTMON ]{f} \n{vm}--=={f}{az}[ cep ]{f} {am}+=>{f} ')
        if len(cep1) == 8:
            url1='https://api.postmon.com.br/v1/cep/{}'.format(cep1)
            res1=requests.get(url1);req1=res1.json()
            resl1="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA cyberPESTE \n[+] by: cyberPESTE{} \n{}-=[complemento]:{}\n-=[bairro]:{}\n-=[cidade]:{}\n-=[logradouro]:{}\n-=[estado_info]:{}\n-=[cep]:{}\n-=[cidade_info]:{}\n-=[estado]:{} {}".format(ng,f,vd,req1['complemento'],req1['bairro'],req1['cidade'],req1['logradouro'],req1['estado_info'],req1['cep'],req1['cidade_info'],req1['estado'],f)
            print(resl1)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')                                 
    elif n1=='2' or n1=='02':
        cep2=input(f'{vm}--=={f}{az}[fonte VIACEP ]{f} \n{vm}--=={f}{az}[ cep ]{f} {am}+=>{f} ')
        if len(cep2)==8:
            url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
            res2 = requests.get(url2);req2=res2.json()
            resl2="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA cyberPESTE \n[+] by: cyberPESTE{} \n{}-=[cep]:{}\n-=[logradouro]:{}\n-=[complemento]:{}\n-=[bairro]:{}\n-=[localidade]:{}\n-=[uf]:{}\n-=[ibge]:{}\n-=[gia]:{} {}".format(ng,f,vd,req2['cep'],req2['logradouro'],req2['complemento'],req2['bairro'],req2['localidade'],req2['uf'],req2['ibge'],req2['gia'],f)        
            print(resl2)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')
    elif n1=='3' or n1=='03':
        cep3=input(f'{vm}--=={f}{az}[fonte APICEP ]{f} \n{vm}--=={f}{az}[ cep ]{f} {am}+=>{f} ')
        if len(cep3) == 8:            
            url3='https://ws.apicep.com/cep/{}.json'.format(cep3) 
            res3 = requests.get(url3);req3=res3.json()
            resl3="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA cyberPESTE \n[+] by: cyberPESTE{} \n{}-=[status]:{}\n-=[ok]:{}\n-=[código]:{}\n-=[estado]:{}\n-=[cidade]:{}\n-=[distrito]:{}\n-=[endereço]:{}\n-=[statusText]:{} {}".format(ng,f,vd,req3['status'],req3['ok'],req3['code'],req3['state'],req3['city'],req3['district'],req3['address'],req3['statusText'],f)
            print(resl3)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')            
def cnpj():    
    cpnj1=input(f'{vm}--=={f}{az}[fonte RECEITA FEDERAL ]{f} \n{vm}--=={f}{az}[ cpnj ]{f} {am}+=>{f} ')                           
    url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
    res=requests.get(url1);req1=res.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    br="\n{}[+] CONSULTA REALIZADA PELO SCRIPT CONSULTA cyberPESTE \n[+]by: cyberPESTE {}\n{}-=[data_situacao]:{}\n-=[motivo_situacao]:{}\n-=[complemento]:{}\n-=[tipo]:{}\n-=[nome]:{}\n-=[telefone]:{}\n-=[situacao]:{}\n-=[bairro]:{}\n-=[logradouro]:{}\n-=[numero]:{}\n-=[cep]:{}\n-=[municipio]:{}\n-=[fantasia]:{}\n-=[porte]:{}\n-=[abertura]:{}\n-=[natureza_juridica]:{}\n-=[uf]:{}\n-=[cnpj]:{}\n-=[ultima_atualizacao]:{}\n-=[status]:{}\n-=[email]:{}\n-=[efr]:{}\n-=[situacao_especial]:{}\n-=[data_situacao_especial]:{}\n-=[atividade_principal]:{}\n-=[atividades_secundarias]:{}\n-=[capital_social]:{}\n-=[qsa]:{}\n-=[extra]:{}\n-=[billing]:{} {}".format(ng,f,vd,req1['data_situacao'],req1['motivo_situacao'],req1['complemento'],req1['tipo'],req1['nome'],req1['telefone'],req1['situacao'],req1['bairro'],req1['logradouro'],req1['numero'],req1['cep'],req1['municipio'],req1['fantasia'],req1['porte'],req1['abertura'],req1['natureza_juridica'],req1['uf'],req1['cnpj'],req1['ultima_atualizacao'],req1['status'],req1['email'],req1['efr'],req1['situacao_especial'],req1['data_situacao_especial'],req1['atividade_principal'],req1['atividades_secundarias'],req1['capital_social'],req1['qsa'],req1['extra'],req1['billing'],f)                  
    print(br)
def ban():
    print(f"""
{vm}    	
              ¤¶¶¶¶¶¶¶¶¶¶¤
          ¤¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¤
        ¤¶¶¶¶¶¶¶¶¤¤¤¤¤¶¶¶¶¶¶¶¶¤
       ¤¶¶¶¶¶¶¶¤¤¤¤¤¤¤¤¤¶¶¶¶¶¶¶¤
      ¤¶¶¶¶¤¶¶¶¶¶¤¤¤¤¤¶¶¶¶¶¤¶¶¶¶¤
      ¤¶¶¶¶¶¤¶¶¶¶¶¤¤¤¶¶¶¶¶¤¶¶¶¶¶¤
      ¤¶__¤¶¶¶¶¶¶¶¶¤¶¶¶¶¶¶¶¶¤__¶¤
      ¤¶_____¤¶¶¶¶¶¶¶¶¶¶¶¤_____¶¤    TEM COISA EM IGRÊSS 
      ¤¶_______¤¶¶¶¶¶¶¶¤_______¶¤   SKSKSKKSKSKSKKS
       ¤¶__________¶¶_________¶¤
        ¤¶¶________¶¶________¶¶¤
         ¤¶¶¶¶¶¶¤______¤¶¶¶¶¶¶¤
      ¤¶¶¤¤¶¶¶¤_________¤¶¶¶¶¤¤¶¶¤
        ¤¶¶¶¶__¶¶¶*¶*¶¶¶__¶¶¶¶¤
               ¤¶¶¶¶¶¶¶¤
    Coded by:   ¤¶¶¤¶¶¤  @cyberPESTE
                 ¶¤¤¤¶     and
                  ¤¶¤     @ravenax
                  ¤¶¤         and
                  ¤¶¤            @cirilo
                  ¶¶¶
                  ¤¶¤
        	  ¤¶¤   
                  ¤¶¤
                  ¤¶¤
                ¤¶¶¤¶¶¤
                 ¤¶¤¶¤
                  ¤¶¤    {f}	                            
                           {ng} consulta cyberPESTE {f} 
  """)
os.system('clear');
def menu():
    print(f"""
{mg}    	

                              _________-----_____ 
                   _____------           __      ----_ 
           ___----             ___------              \ 
              ----________        ----                 \ 
                          -----__    |             _____) 
                               __-                /#####\ 
                   _______-----    ___--          \####/)\ 
             ------_______      ---____            \##/  / 
                          -----__    \ --    _      --   /\   
                                 --__--__     \_____/   \_/\ 
                                        ----|   /          | 
                                            |  |___________| 
  +55 32 84939274 chama...	            |  | ((_(_)| )_) 
  				            |  \_((_(_)|/(_) 
                                            \             ( 
					     \_____________) 
					      	{vd}   			       
		           _____  _____ ____ _____ _____ 
  ___ _   _| |__   ___ _ __|  _ \| ____/ ___|_   _| ____|    
 / __| | | | '_ \ / _ \ '__| |_) |  _| \___ \ | | |  _|      
| (__| |_| | |_) |  __/ |  |  __/| |___ ___) || | | |___     
 \___|\__, |_.__/ \___|_|  |_|   |_____|____/ |_| |_____|,    
      |___/      {f}
   {am}    and and and and and and and and {f}  
                 {mg} 
      _ __ __ ___   _____ _ __   __ ___  __
     | '__/ _` \ \ / / _ \ '_ \ / _` \ \/ /
     | | | (_| |\ V /  __/ | | | (_| |>  < 
     |_|  \__,_| \_/ \___|_| |_|\__,_/_/\_\  {f} 		       
	{am}	and and and and and and and and			 	       
{vd}
╔═══╗╔══╗╔═══╗╔══╗╔╗───╔═══╗
║╔═╗║╚╣─╝║╔═╗║╚╣─╝║║───║╔═╗║
║║─╚╝─║║─║╚═╝║─║║─║║───║║─║║
║║─╔╗─║║─║╔╗╔╝─║║─║║─╔╗║║─║║
║╚═╝║╔╣─╗║║║╚╗╔╣─╗║╚═╝║║╚═╝║
╚═══╝╚══╝╚╝╚═╝╚══╝╚═══╝╚═══╝
 {f}
                     
   	 	       
- {ng}01 CONSULTAR IP {f}
- {ng}02 CONSULTAR CEP {f}
- {ng}03 CONSULTAR CNPJ {f}
- {ng}04 SAIR{f}
    """)
try:   
    menu()
    inpu=str(input(f'- {am}=+>{f} '))
except KeyboardInterrupt:
    exit()
except:
    print(f""" {vm}
                       // ¤ \\
                       \\ ¤ //
                         \\//
                        (___)                    
                        (___)
                        (___)
      \_____/\__/     \__/ \_____/
        \ _ ​[     ​. *       ​*     ]​ _ /
                \_𓬞 *          * _/
                   . \ __°__ /.
                       |\_°_/|
  CP                    [|\_/|]
      RX                [|[¤]|]
    CR                  [|;¤;|]
                        [;;¤;;]
                       ;;;;¤]|]\
                      ;;;;;¤]|]-\
                     ;;;;;[¤]|]--\
                    ;;;;;|[¤]|]---\
                   ;;;;;[|[¤]|]|---|
                  ;;;;;[|[¤]|]|---|
                  ;;;;[|[¤]|/---/
                  ;;;[|[¤]/---/
                  ;;[|[¤/---/
                    ;[|[/---/
                    [|/---/
                    /---/
                   /---/|]
                 /---/]|];
               /---/¤]|]
              |---|[¤]|];;;
              |---|[¤]|];;;;
               \--|[¤]|];;;;     
                 \-|[¤]|];;;;
                   \|[¤]|];;;
                     \\¤//
                       \|/
   C COLOCOU ERRADO ZÉ!{f}');exit()                                                             
        
    
    
except:
    exit()
       
       

  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

