import sqlite3

import sqlite3 as sql

database = "paciente.db"

conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS paciente (nome TEXT,codigo INTEGER PRIMARY KEY, endereco TEXT, cpf TEXT, observacao TEXT)")
conn.commit()
conn.close()


class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "CREATE TABLE IF NOT EXISTS clientes (nome TEXT,codigo INTEGER PRIMARY KEY, endereco TEXT, cpf TEXT, observacao TEXT)")
    trans.persist()
    trans.disconnect()

initDB()


def view():
    trans = TransactionObject()
    trans.connect()

    trans.execute("SELECT * FROM paciente")

    rows = trans.fetchall()
    trans.disconnect()
    return rows


def insert(nome, codigo, endereco, cpf, observacao):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO paciente VALUES(NULL, ?,?,?,?)", (nome, codigo, endereco, cpf, observacao))
    trans.persist()
    trans.disconnect()

def search(nome="", codigo="", endereco="", cpf="", observacao=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM paciente WHERE nome=? or endereco=? or cpf=? or observacao=?", nome, codigo, endereco, cpf, observacao)
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def update(nome, codigo, endereco, cpf, observacao):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE paciente SET nome =?, endereco=?, cpf=?, observacao=? WHERE codigo=?",(nome, codigo, endereco,cpf, observacao))
    trans.persist()
    trans.disconnect()

def delete(codigo):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM paciente WHERE codigo = ?", (codigo,))
    trans.persist()
    trans.disconnect()