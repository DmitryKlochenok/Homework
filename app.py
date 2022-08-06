from flask import Flask
import json


def load_candidates():
   """
  Загружает данные из файла
   """
   global candidates
   with open("candidates.json","r", encoding="utf-8") as file:
      candidates = json.load(file)


def get_all():
   """
   Показывает всех кандидатов из файла
   """
   print("Кандидаты:")
   names_list = []
   for item in candidates:
      names_list.appent(item["name"])

   return names_list


def get_by_pk(pk):
   """
   Возвращает кандидата по pk
   """
   for item in candidates:
      if item["pk"] == pk:
         return item


def get_by_skill(skill_name):
   """
   Возвращает кандидатов по навыку
   """
   global list_by_skills
   list_by_skills = []
   for item in candidates:
      if skill_name.lower() in item["skills"].lower():
         list_by_skills.append(item)
   return list_by_skills


load_candidates()


app = Flask(__name__)

@app.route("/")
def page_index():
   cand_list = []
   for item in candidates:
      text = f"""
      <pre>
      Имя кандидата: {item['name']}<br/>
      Позиция: {item['position']}<br/>
      Навыки: {item['skills']}<br/>
      </pre>
      """
      cand_list.append(text)
   return '<br/>'.join(cand_list)


@app.route("/candidates/<int:x>/")
def page_candidates(x):
   cand = get_by_pk(x)
   url = cand['picture']
   text = f"""
   <img src='({url})'>
   <pre>
  Имя кандидата: {cand["name"]}-
  Позиция кандидата: {cand["position"]}
  Навыки: {cand["skills"]}
</pre>
  """
   return text


@app.route("/skills/<x>/")
def page_skills(x):
   y = x.lower()
   get_by_skill(y)
   by_skills_list = []
   for item in list_by_skills:
      text = f"""
            <pre>
            Имя кандидата: {item['name']}<br/>
            Позиция: {item['position']}<br/>
            Навыки: {item['skills']}<br/>
            </pre>
            """
      by_skills_list.append(text)
   return '<br/>'.join(by_skills_list)



app.run()