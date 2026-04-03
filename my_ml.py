import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


data_path = 'melb_data.csv'
data = pd.read_csv(data_path)
data = data.dropna(axis=0)
data.columns = data.columns.str.strip()


y = data.Price
data_fields = [
    'Rooms',
    'Bathroom',
    'Landsize',
    'Lattitude',
    'Longtitude'
]
x = data[data_fields]

# разбтение данных на тренировочные и проверочные
x_train, x_data, y_train, y_data = train_test_split(x, y, random_state=0)


# модель с лесом(множесто деревьев) и расчет предикта
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(x_train, y_train)
forest_pred = forest_model.predict(x_data)
print(mean_absolute_error(y_data, forest_pred))





# модель расчета предикта
# model = DecisionTreeRegressor()
# model.fit(x_train, y_train)
# pred = model.predict(x_data)
# print(mean_absolute_error(y_data, pred))



# функция расета предикта и проверки ошибок обучения на кол-во нодов
# def get_mae(max_leaf_nodes, x_train, x_data, y_train, y_data):
#     model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
#     model.fit(x_train, y_train)
#     predict_x = model.predict(x_data)
#     mae = mean_absolute_error(y_data, predict_x)
#     return(mae)

# for max_leaf_nodes in [5, 50, 500, 5000]:
#     my_mae = get_mae(max_leaf_nodes, x_train, x_data, y_train, y_data)
#     print(f"Max leaf nodes: {max_leaf_nodes}\t\t Mean Absolute Error: {my_mae}")


# print("Making predictions for the following 5 houses:")
# print(x.head())
# print("Predictions:")
# print(melbourne_model.predict(x.head()))
# вычисление ошибки модели
# predicted_home_prices = model.predict(x)
# mean_absolute_error(y, predicted_home_prices)