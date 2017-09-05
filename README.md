### flask-sqlalchemy-multidb-example

Add `SQLALCHEMY_BINDS` to `app.config`.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test1'
app.config['SQLALCHEMY_BINDS'] = {
    'test2': 'mysql+pymysql://root:root@localhost:3306/test2',
    'test1': 'mysql+pymysql://root:root@localhost:3306/test1'
}
```
Default is `SQLALCHEMY_DATABASE_URI`. If not set `__bind_key__`, default binding is `SQLALCHEMY_DATABASE_URI`.

```python
class User(db.Model):
    __tablename__ = "tb_user"
    __bind_key__ = 'test2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Store(db.Model):
    __tablename__ = "tb_store"
    __bind_key__ = 'test1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, primary_key=True)
```

