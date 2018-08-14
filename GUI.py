from tkinter import *


class Gui():

    window = Tk()
    window.wm_title("Cadastro de Pacientes")

    txtNome = StringVar()
    lblnome = Label(window,text = "Nome")
    lblnome.grid(row=0, column=0)
    entNome = Entry(window, textvariable = txtNome)
    entNome.grid(row=0, column=1, padx=50, pady=50)

    txtCodigo = StringVar()
    lblcodigo = Label(window, text = "Código")
    lblcodigo.grid(row=1, column=0)
    entCodigo = Entry(window, textvariable=txtCodigo)
    entCodigo.grid(row=1, column=1)

    txtEndereco = StringVar()
    lblendereco = Label(window, text = "Endereço")
    lblendereco.grid(row=2, column=0)
    entEndereco = Entry(window, textvariable=txtEndereco)
    entEndereco.grid(row=2, column=1)

    txtCPF = StringVar()
    lblcpf = Label(window, text="CPF")
    lblcpf.grid(row=3, column=0)
    entCPF = Entry(window, textvariable=txtCPF)
    entCPF.grid(row=3, column=1)

    txtObservacao = StringVar()
    lblobservacao = Label(window, text = "Observação")
    lblobservacao.grid(row=4, column=0)
    entObservacao = Entry(window, textvariable=txtObservacao)
    entObservacao.grid(row=4, column=1)


    listPacientes = Listbox(window)
    listPacientes.grid(row=0, column=2, rowspan=10)

    scrollPacientes = Scrollbar(window)
    scrollPacientes.grid(row=0, column=6, rowspan=10)

    btnVerTodos = Button(window, text = "Ver Todos")
    btnVerTodos.grid(row=5, column=0, columnspan=2)

    btnBuscar = Button(window, text="Buscar")
    btnBuscar.grid(row=6, column=0, columnspan=2)

    btnInserir = Button(window, text="Inserir")
    btnInserir.grid(row=7, column=0, columnspan=2)

    btnAtualizar = Button(window, text= "Atualizar")
    btnAtualizar.grid(row=8, column=0, columnspan=2)

    btnDelete = Button(window, text = "Deletar")
    btnDelete.grid(row=9, column=0, columnspan=2)

    btnFechar = Button(window, text = "Fechar")
    btnFechar.grid(row=10, column=0, columnspan=2)

    # Associando a Scrollbar com a Listbox...
    listPacientes.configure(yscrollcommand=scrollPacientes.set)
    scrollPacientes.configure(command=listPacientes.yview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    # Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')


    window.mainloop()