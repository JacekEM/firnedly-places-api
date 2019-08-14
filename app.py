import os

from models import Restaurant

import config


if not os.path.exists('./restaurants.db'):
    example_restaurant_data = {'name': 'ExampleRes', 'address': 'Skargi 2 ', 'phone': 1111111, 'web': 'googleit'}
    config.db.create_all()
    example_res = Restaurant(name=example_restaurant_data['name'],
                             address=example_restaurant_data['address'],
                             phone=example_restaurant_data['phone'],
                             web=example_restaurant_data['web']
                             )
    config.db.session.add(example_res)
    config.db.session.commit()


app = config.con_app
app.add_api('3.0.1-swagger.yml')


@app.route('/')
def hello_world():
    return 'navigate to \'/api/ui\''


if __name__ == "__main__":
    app.run(debug=True)