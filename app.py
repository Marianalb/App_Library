from model.DataJSon import JSon
import DAO.Requisitar_DAO
import DAO.Devolver_DAO
import DAO.Adicionar_DAO
import DAO.Atualizar_DAO
import DAO.Remover_DAO
import DAO.Guardar_DAO
import DAO.Info_DAO
import __builtin__
clients_file = JSon("/media/sf_VMshared/Refactoring1/Resources/Clients.json")
data = clients_file.read()
__builtin__.clients = data

book_file = JSon("/media/sf_VMshared/Refactoring1/Resources/Book")
data = book_file.read()
__builtin__.books = data

f = JSon("/media/sf_VMshared/Refactoring1/Resources/Reservas.json")
global data_reser
__builtin__.data_reser = f.read()

if __name__ == "__main__":

    while True:
        print "Actual clients: {}".format(__builtin__.clients)
        print "Actual available books: {}".format(__builtin__.books)
        print "Opcoes:\n1 - Requesitar\n2 - Devolver\n3 - Adicionar\n4 - Atualizar\n5 - Eleminar\n6 - Guardar"


        option = raw_input(">> ")

        if(option == '1'):
            client_name = raw_input("Nome de registo (client name):").lower()
            book_name = raw_input("Nome do livro a requisitar:").lower()
            DAO.Requisitar_DAO.Requisitar(book_name, client_name)

        elif(option == '2'):
            client_name = raw_input("Nome de entrega (client name):").lower()
            book_name = raw_input("Nome do livro a requisitar:").lower()
            DAO.Devolver_DAO.Devolver(book_name, client_name)

        elif(option == '3'):
            book_name = raw_input("Nome do livro a adicionar:").lower()
            DAO.Adicionar_DAO.Adicionar(book_name)

        elif(option == '4'):
            book_name = raw_input("Nome do livro:").lower()
            new_book_name = raw_input("Nome do livro atualizado:")
            DAO.Atualizar_DAO.Atualizar(book_name,new_book_name)


        elif(option == '5'):
            book_name = raw_input("Nome do livro a remover:").lower()
            DAO.Remover_DAO.Remover(book_name)

        elif(option == "6"):
            DAO.Guardar_DAO.Guardar(clients_file,book_file,f)

        else:
            print("Nao foi uma opcao valida")

