import xml.etree.ElementTree as ET
from logging_config import LOGGER, ini_logging

# XML fornecido
xml_data = '''<?xml version='1.0' encoding='UTF-8'?>
<rss version='2.0'>
  <channel>
    <title>Instituto Português do Mar e da Atmosfera, I.P. - Comunicados</title>
    <link>https://www.ipma.pt</link>
    <description>Últimos Comunicados Emitidos</description>
    <lastBuildDate>2024-10-04 07:17:33</lastBuildDate>
    <copyright>Copyright (C) Instituto Português do Mar e da Atmosfera, I.P. 2024</copyright>
    <language>pt-pt</language>
    <managingEditor>info@ipma.pt (IPMA,IP-Informações)</managingEditor>
    <image>
      <title>Instituto Português do Mar e da Atmosfera</title>
      <link>https://www.ipma.pt</link>
      <url>https://www.ipma.pt/bin/icons/svg/logo-ipma-rss.svg</url>
    </image>
    <item>
      <title>Aviso de Sismo no Continente  02-10-2024  15:26</title>
      <link>https://www.ipma.pt/pt/geofisica/comunicados/</link>
      <pubDate>2024-10-02 14:56:25</pubDate>
      <description>&lt;table style=&quot;width:470px; text-align:center&quot; border=&quot;0&quot; cellpadding=&quot;1&quot; cellspacing=&quot;0&quot; &gt; &lt;tr&gt;&lt;td style=&quot;height:1; bgcolor:#BCD1DF&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:30px; background-color:#E4EDF2; text-align:center; vertical-align:middle&quot;&gt;&lt;b&gt;Informação  Sismológica&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot; &gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:10px&quot;&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:20px; text-align:center; vertical-align:middle&quot;&gt;&lt;em&gt;Titulo:&lt;/em&gt; &lt;b&gt;Aviso de Sismo no Continente  02-10-2024  15:26&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;text-align:justify; vertical-align:top&quot;&gt;&lt;br/&gt;O Instituto Português do Mar e da Atmosfera informa que no dia 02-10-2024 pelas 15:26 (hora local) foi registado nas estações da Rede Sísmica do Continente, um sismo de magnitude 2.6 (Richter) e cujo epicentro se localizou a cerca de 14 km a Norte-Nordeste de Vendas Novas.&lt;br/&gt;Até à  elaboração deste comunicado não foi recebida nenhuma informação confirmando que este sismo tenha sido sentido.&lt;br/&gt;Se a situação o justificar serão emitidos novos comunicados.&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;A localização do epicentro de um sismo é um processo físico e matemático complexo que depende do conjunto de dados, dos algoritmos e dos modelos de propagação das ondas sísmicas. Agências diferentes podem produzir resultados ligeiramente diferentes. Do mesmo modo, as determinações preliminares são habitualmente corrigidas posteriormente, pela integração de mais informação. Em todos os casos acompanhe sempre as indicações dos serviços de proteção civil. Toda e qualquer utilização do conteúdo deste comunicado deverá sempre fazer referência à fonte.&lt;br/&gt;&lt;br/&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr style=&quot;vertical-align:middle&quot;&gt;    &lt;td style=&quot;text-align:center; vertical-align:middle&quot;&gt;&lt;small&gt;&lt;em&gt;Data de Edição:&lt;/em&gt; &lt;b&gt;Qua, 02 Out 2024 14:55:25&lt;/b&gt;&lt;/small&gt;&lt;/td&gt;  &lt;/tr&gt;&lt;/table&gt;</description>
    </item>
    <item>
      <title>Aviso de Sismo no Continente  02-10-2024  15:26</title>
      <link>https://www.ipma.pt/pt/geofisica/comunicados/</link>
      <pubDate>2024-10-02 14:55:25</pubDate>
      <description>&lt;table style=&quot;width:470px; text-align:center&quot; border=&quot;0&quot; cellpadding=&quot;1&quot; cellspacing=&quot;0&quot; &gt; &lt;tr&gt;&lt;td style=&quot;height:1; bgcolor:#BCD1DF&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:30px; background-color:#E4EDF2; text-align:center; vertical-align:middle&quot;&gt;&lt;b&gt;Informação  Sismológica&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot; &gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:10px&quot;&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:20px; text-align:center; vertical-align:middle&quot;&gt;&lt;em&gt;Titulo:&lt;/em&gt; &lt;b&gt;Aviso de Sismo no Continente  02-10-2024  15:26&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;text-align:justify; vertical-align:top&quot;&gt;&lt;br/&gt;O Instituto Português do Mar e da Atmosfera informa que no dia 02-10-2024 pelas 15:26 (hora local) foi registado nas estações da Rede Sísmica do Continente, um sismo de magnitude 2.6 (Richter) e cujo epicentro se localizou a cerca de 14 km a Norte-Nordeste de Vendas Novas.&lt;br/&gt;Até à  elaboração deste comunicado não foi recebida nenhuma informação confirmando que este sismo tenha sido sentido.&lt;br/&gt;Se a situação o justificar serão emitidos novos comunicados.&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;A localização do epicentro de um sismo é um processo físico e matemático complexo que depende do conjunto de dados, dos algoritmos e dos modelos de propagação das ondas sísmicas. Agências diferentes podem produzir resultados ligeiramente diferentes. Do mesmo modo, as determinações preliminares são habitualmente corrigidas posteriormente, pela integração de mais informação. Em todos os casos acompanhe sempre as indicações dos serviços de proteção civil. Toda e qualquer utilização do conteúdo deste comunicado deverá sempre fazer referência à fonte.&lt;br/&gt;&lt;br/&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr style=&quot;vertical-align:middle&quot;&gt;    &lt;td style=&quot;text-align:center; vertical-align:middle&quot;&gt;&lt;small&gt;&lt;em&gt;Data de Edição:&lt;/em&gt; &lt;b&gt;Qua, 02 Out 2024 14:55:25&lt;/b&gt;&lt;/small&gt;&lt;/td&gt;  &lt;/tr&gt;&lt;/table&gt;</description>
    </item>
    <item>
      <title>Aviso de Sismo no Continente  02-10-2024  15:26</title>
      <link>https://www.ipma.pt/pt/geofisica/comunicados/</link>
      <pubDate>remover</pubDate>
      <description>&lt;table style=&quot;width:470px; text-align:center&quot; border=&quot;0&quot; cellpadding=&quot;1&quot; cellspacing=&quot;0&quot; &gt; &lt;tr&gt;&lt;td style=&quot;height:1; bgcolor:#BCD1DF&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:30px; background-color:#E4EDF2; text-align:center; vertical-align:middle&quot;&gt;&lt;b&gt;Informação  Sismológica&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot; &gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:10px&quot;&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:20px; text-align:center; vertical-align:middle&quot;&gt;&lt;em&gt;Titulo:&lt;/em&gt; &lt;b&gt;Aviso de Sismo no Continente  02-10-2024  15:26&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;text-align:justify; vertical-align:top&quot;&gt;&lt;br/&gt;O Instituto Português do Mar e da Atmosfera informa que no dia 02-10-2024 pelas 15:26 (hora local) foi registado nas estações da Rede Sísmica do Continente, um sismo de magnitude 2.6 (Richter) e cujo epicentro se localizou a cerca de 14 km a Norte-Nordeste de Vendas Novas.&lt;br/&gt;Até à  elaboração deste comunicado não foi recebida nenhuma informação confirmando que este sismo tenha sido sentido.&lt;br/&gt;Se a situação o justificar serão emitidos novos comunicados.&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;A localização do epicentro de um sismo é um processo físico e matemático complexo que depende do conjunto de dados, dos algoritmos e dos modelos de propagação das ondas sísmicas. Agências diferentes podem produzir resultados ligeiramente diferentes. Do mesmo modo, as determinações preliminares são habitualmente corrigidas posteriormente, pela integração de mais informação. Em todos os casos acompanhe sempre as indicações dos serviços de proteção civil. Toda e qualquer utilização do conteúdo deste comunicado deverá sempre fazer referência à fonte.&lt;br/&gt;&lt;br/&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr style=&quot;vertical-align:middle&quot;&gt;    &lt;td style=&quot;text-align:center; vertical-align:middle&quot;&gt;&lt;small&gt;&lt;em&gt;Data de Edição:&lt;/em&gt; &lt;b&gt;Qua, 02 Out 2024 14:55:25&lt;/b&gt;&lt;/small&gt;&lt;/td&gt;  &lt;/tr&gt;&lt;/table&gt;</description>
    </item>
    <item>
      <title>Aviso de Sismo Sentido no Arquipélago dos Açores  02-10-2024  10:35</title>
      <link>https://www.ipma.pt/pt/geofisica/comunicados/</link>
      <pubDate>teste_dup</pubDate>
      <description>&lt;table style=&quot;width:470px; text-align:center&quot; border=&quot;0&quot; cellpadding=&quot;1&quot; cellspacing=&quot;0&quot; &gt; &lt;tr&gt;&lt;td style=&quot;height:1; bgcolor:#BCD1DF&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:30px; background-color:#E4EDF2; text-align:center; vertical-align:middle&quot;&gt;&lt;b&gt;Informação  Sismológica&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot; &gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:10px&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;height:20px; text-align:center; vertical-align:middle&quot;&gt;&lt;em&gt;Titulo:&lt;/em&gt; &lt;b&gt;Aviso de Sismo Sentido no Arquipélago dos Açores  02-10-2024  10:35&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;    &lt;td style=&quot;text-align:justify; vertical-align:top&quot;&gt;&lt;br/&gt;O Instituto Português do Mar e da Atmosfera informa que no dia 02-10-2024 pelas 10:35 (hora local) foi registado nas estações da Rede Sísmica do Arquipélago dos Açores, um sismo de magnitude 2.1 (Richter) e cujo epicentro se localizou próximo de Pedro Miguel (Faial).&lt;br/&gt;Este sismo, de acordo com a informação disponível até ao momento, não causou danos pessoais ou materiais e foi sentido com intensidade máxima III (escala de Mercalli modificada) na freguesia de Praia de Almoxarife (Horta).&lt;br/&gt;Se a situação o justificar serão emitidos novos comunicados.&lt;br/&gt;&lt;br/&gt;A localização do epicentro de um sismo é um processo físico e matemático complexo que depende do conjunto de dados, dos algoritmos e dos modelos de propagação das ondas sísmicas. Agências diferentes podem produzir resultados ligeiramente diferentes. Do mesmo modo, as determinações preliminares são habitualmente corrigidas posteriormente, pela integração de mais informação. Em todos os casos acompanhe sempre as indicações dos serviços de proteção civil. Toda e qualquer utilização do conteúdo deste comunicado deverá sempre fazer referência à fonte.&lt;br/&gt;&lt;br/&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;&lt;td style=&quot;height:1px; background-color:#BCD1DF;&quot;&gt;&lt;/td&gt;&lt;/tr&gt;  &lt;tr style=&quot;vertical-align:middle&quot;&gt;    &lt;td style=&quot;text-align:center; vertical-align:middle&quot;&gt;&lt;small&gt;&lt;em&gt;Data de Edição:&lt;/em&gt; &lt;b&gt;Qua, 02 Out 2024 11:51:12&lt;/b&gt;&lt;/small&gt;&lt;/td&gt;  &lt;/tr&gt;&lt;/table&gt;</description>
    </item>
  </channel>
</rss>'''



# Verificar se o item já foi descarregado
def verifica_duplicados(item):
  pub_date = item.find('pubDate').text
  #if pub_date == 'remover'
  with open('historico.txt', 'r') as file:
    for line in file:
      if line.strip() == pub_date:
        return True
  return False
  
  
  return pub_date == 'remover'


def registaHistoria(item):
  pub_date = item.find('pubDate').text
  with open('historico.txt', 'a') as file:
    file.write(f"{pub_date}\n")
  LOGGER.info(f"Item {item.find('title').text} registado com data {pub_date}")
  pass
  
  

def main():
  ini_logging()
  LOGGER.debug('sandBox started')
  
  # Parse the XML
  root = ET.fromstring(xml_data)
  LOGGER.debug(f"XML parced: {root}")
  
  # Encontrar todos os itens no XML
  items = root.findall('.//item')
  LOGGER.debug(f"Items: {items}")
    
    
  # Iterar sobre os itens e remover aqueles com pubDate igual a 
  # 'teste_dup'
  # a ideia e verificar se o item ja tinha sido descarregado
  # e se sim remover, eliminando assim duplicados.
  # Ainda falta defenir como guardar este hisrorico
  # e como verificar se o item ja foi descarregado
  for item in items:
      #verifica_duplicados(item)
      #pub_date = item.find('pubDate').text
      #if pub_date == 'remover':
    LOGGER.info(f"Item {item.find('title').text} com data {item.find('pubDate').text}")
    if verifica_duplicados(item):
      LOGGER.info(f"Item {item.find('title').text} já foi descarregado")
      root.find('.//channel').remove(item)
    else:
      LOGGER.info(f"Item {item.find('title').text} não foi descarregado")
      registaHistoria(item)
    
          
          
  #todo: guardar historico
  #todo: verifica se o numero de items e zero
  # se sim não guarda ficheiro
  # se não guarda a extração completa do xml
  modified_xml = ET.tostring(root, encoding='unicode')
  #print(modified_xml)

  with open('output.xml', 'wb') as file:
    file.write(modified_xml.encode('utf-8'))
    
  
  
 
    
if __name__ == '__main__':
    main()