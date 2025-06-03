# DB

| Name                             | Properties                       | Description                                                                                          |
|----------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------|
| `APP_CONFIG__DB__URL`            | **Required**                     |                                                                                                      |
| `APP_CONFIG__DB__ECHO`           | *Optional* <br> default=`False`  | Логирование SQL запросов                                                                             | 
| `APP_CONFIG__DB__ECHO_POOL`      | *Optional* <br> default=`False`  | Логирование работы пула соединения                                                                   | 
| `APP_CONFIG__DB__POOL_SIZE`      | *Optional* <br> default=`50`     | Размер пула соединений                                                                               | 
| `APP_CONFIG__DB__MAX_OVERFLOW`   | *Optional* <br> default=`10`     | количество дополнительных соединений, которые могут быть созданы сверх `pool_size`,  если все заняты |


# API


| Name                      | Properties                           | Description |
|---------------------------|--------------------------------------|-------------|
| `APP_CONFIG__API__PREFIX` | *Optional* <br> default=`/api`       |             |


# RUN

| Name                       | Properties                        | Description |
|----------------------------|-----------------------------------|-------------|
| `APP_CONFIG__RUN__HOST`    | *Optional* <br> default=`0.0.0.0` |             |
| `APP_CONFIG__RUN__PORT`    | *Optional* <br> default=`8000`    |             |