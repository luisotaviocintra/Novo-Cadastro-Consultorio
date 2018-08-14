from GUI import *
import Backend as core

app = None
app = Gui()

def view_command():
    rows = core.view()
    app.listPacientes.delete(0, END)
    for r in rows:
        app.listPacientes.insert(END, r)

def search_command():
    app.listPacientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtCodigo.get(), app.txtEndereco.get(), app.txtCPF.get(), app.txtObservacao.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
            core.insert(app.txtNome.get(), app.txtCodigo.get(), app.txtEndereco.get(), app.txtCPF.get(), app.txtObservacao.get())
            view_command()

def getSelectedRow(event):
    global selected
    index = app.listPacientes.curselection()[0]
    selected = app.listPacientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entCodigo.delete(0, END)
    app.entCodigo.insert(END, selected[2])
    app.entEndereco.delete(0, END)
    app.entEndereco.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    app.entObservacao.delete(0, END)
    app.entObservacao.insert(END, selected[5])

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtCodigo.get(), app.txtEndereco.get(), app.txtCPF.get(), app.txtObservacao.get())
    view_command()

def del_command():
    codigo = selected[2]
    core.delete(codigo)
    view_command()

app.btnVerTodos.configure(command=view_command)
app.btnBuscar.configure(command=search_command)
app.btnInserir.configure(command=insert_command)
app.btnAtualizar.configure(command=update_command)
app.btnDelete.configure(command=del_command)
app.btnFechar.configure(command=app.window.destroy)

app.listPacientes.bind('<<ListboxSelect>>', getSelectedRow)


app.run()
