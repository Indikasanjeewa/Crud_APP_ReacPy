from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

from reactpy import component, html, run


@component
def App():
     return html.h1("Hello, world!")

from reactpy import component, html, run


@component
def DataList(items, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority is not None:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = sorted(items, key=lambda i: i["priority"])
    list_item_elements = [html.li({"key": i["id"]}, i["text"]) for i in items]
    return html.ul(list_item_elements)


@component
def TodoList():
    tasks = [
        {"id": 0, "text": "breakfast", "priority": 0},
        {"id": 1, "text": "Feed the dog", "priority": 0},
        {"id": 2, "text": "Do laundry", "priority": 2},
        {"id": 3, "text": "Go on a run", "priority": 1},
        {"id": 4, "text": "Clean the house", "priority": 2},
        {"id": 5, "text": "Go to the grocery store", "priority": 2},
        {"id": 6, "text": "Do some coding", "priority": 1},
        {"id": 7, "text": "Read a book", "priority": 1},
    ]
    return html.section(
        html.h1("ReactPy"),
        html.p("ReactPy is a library for building user interfaces in Python without Javascript. ReactPy interfaces are made from components which look and behave similarly to those found in ReactJS. Designed with simplicity in mind, ReactPy can be used by those without web development experience while also being powerful enough to grow with your ambitions."),
        html.h1("Learning ReactPy"),
        html.p("This documentation is broken up into chapters and sections that introduce you to concepts step by step with detailed explanations and lots of examples. You should feel free to dive into any content that seems interesting. While each chapter assumes knowledge from those that came before, when you encounter a concept you’re unfamiliar with you should look for links that will help direct you to the place where it was originally taught."),
        html.h1("My Todo List"),
        
        DataList(tasks, filter_by_priority=1, sort_by_priority=True),
    )


run(TodoList)

      
run(App)

