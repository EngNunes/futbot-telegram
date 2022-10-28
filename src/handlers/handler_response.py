from constants.groups import groups_pt, groups_en, groups_es
from constants.champions import champions_pt, champions_en, champions_es

def handle_response(text) -> str:
  
  ##Groups PT
  if 'a' == text.lower() or 'grupo a' == text.lower():
    return groups_pt[0]  #A
  if 'b' == text.lower() or 'grupo b' == text.lower():
    return groups_pt[1]  #B
  if 'c' == text.lower() or 'grupo c' == text.lower():
    return groups_pt[2]  #C
  if 'd' == text.lower() or 'grupo d' == text.lower():
    return groups_pt[3]  #D
  if 'e' == text.lower() or 'grupo e' == text.lower():
    return groups_pt[4]  #E
  if 'f' == text.lower() or 'grupo f' == text.lower():
    return groups_pt[5]  #F
  if 'g' == text.lower() or 'grupo g' == text.lower():
    return groups_pt[6]  #G
  if 'h' == text.lower() or 'grupo h' == text.lower():
    return groups_pt[7]  #H
  
  ##Group EN
  if 'group a' == text.lower():
    return groups_en[0]  #A
  if 'group b' == text.lower():
    return groups_en[1]  #B
  if  'group c' == text.lower():
    return groups_en[2]  #C
  if 'group d' == text.lower():
    return groups_en[3]  #D
  if 'group e' == text.lower():
    return groups_en[4]  #E
  if 'group f' == text.lower():
    return groups_en[5]  #F
  if 'group g' == text.lower():
    return groups_en[6]  #G
  if 'group h' == text.lower():
    return groups_en[7]  #H
  
  ##Group ES
  if 'elgrupo a' == text.lower():
    return groups_es[0]  #A
  if 'elgrupo b' == text.lower():
    return groups_es[1]  #B
  if  'elgrupo c' == text.lower():
    return groups_es[2]  #C
  if 'elgrupo d' == text.lower():
    return groups_es[3]  #D
  if 'elgrupo e' == text.lower():
    return groups_es[4]  #E
  if 'elgrupo f' == text.lower():
    return groups_es[5]  #F
  if 'elgrupo g' == text.lower():
    return groups_es[6]  #G
  if 'elgrupo h' == text.lower():
    return groups_es[7]  #H
  
  ##Champions PT
  if 'campea brasil' == text.lower():
    return champions_pt[0] #campea Brasil
  if 'campea itália' == text.lower() or 'campea italia' == text.lower():
    return champions_pt[1] #campea Italia
  if 'campea alemanha' == text.lower():
    return champions_pt[2] #campea Alemanha
  if 'campea argentina' == text.lower():
    return champions_pt[3] #campea Argentina
  if 'campea uruguai' == text.lower():
    return champions_pt[4] #campea Franca
  if 'campea franca' == text.lower() or 'campea frança' == text.lower():
    return champions_pt[5] #campea Franca
  if 'campea espanha' == text.lower():
    return champions_pt[6] #campea Espanha
  if 'campea inglaterra' == text.lower():
    return champions_pt[7] #campea Inglaterra
  
  ##Champions EN
  if 'champion brazil' == text.lower():
    return champions_en[0] 
  if 'champion italy' == text.lower():
    return champions_en[1] 
  if 'champion germany' == text.lower():
    return champions_en[2] 
  if 'champion argentina' == text.lower():
    return champions_en[3] 
  if 'champion uruguay' == text.lower():
    return champions_en[4] 
  if 'champion france' == text.lower():
    return champions_en[5] 
  if 'champion spain' == text.lower():
    return champions_en[6] 
  if 'champion england' == text.lower():
    return champions_en[7] 
  
  ##Champions ES
  if 'campeon brasil' == text.lower():
    return champions_es[0] 
  if 'campeon italia' == text.lower():
    return champions_es[1] 
  if 'campeon alemania' == text.lower():
    return champions_es[2] 
  if 'campeon argentina' == text.lower():
    return champions_es[3] 
  if 'campeon uruguay' == text.lower():
    return champions_es[4] 
  if 'campeon francia' == text.lower():
    return champions_es[5] 
  if 'campeon españa' == text.lower():
    return champions_es[6] 
  if 'campeon inglaterra' == text.lower():
    return champions_es[7] 
  
  else:
    return "🤔 Desculpe, não entendi ||| Disculpe, no entendí ||| Sorry, i do not understand"