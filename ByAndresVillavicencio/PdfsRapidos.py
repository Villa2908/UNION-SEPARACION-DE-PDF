import PyPDF2
from tkinter import filedialog
import tkinter
from os.path import basename

#------------------UNIDOR DE PDFS------------------#

unido = PyPDF2.PdfMerger()
selecionados  = []

def AggPdf() -> None:
    try:
        pdfs = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
        for i in pdfs:
            selecionados.append(i)
            lst.insert(tkinter.END, basename(i))
            
    except:
        
        tkinter.messagebox.showinfo("Algo salió mal!", "Parece que ocurrió un error, intentalo de nuevo.")
        
def UnirPdf() -> None:
    try:
        for i in selecionados:
            unido.append(i)
        
        lst.delete(0, tkinter.END)
        nombreNuevo = filedialog.asksaveasfile(defaultextension=".pdf", filetypes=[("Archivo PDF" , "*.pdf")]).name
        unido.write(nombreNuevo)
        unido.close()
        tkinter.messagebox.showinfo("FELICIDADES!", "la union ha sido todo un exito.".title())
    except:
        tkinter.messagebox.showinfo("Algo salio mal!", "Parece que ocurrió un error, intentalo de nuevo.")

def delLst():
    try:
        seleccion = lst.curselection()
        if seleccion != "":
            for i in reversed(seleccion):
                lst.delete(i, i)
            for i in selecionados:
                if seleccion == basename(i):
                    selecionados.remove(i)
                    print(selecionados)
    except tkinter.TclError:
        pass
    except ValueError:
        tkinter.messagebox.showinfo("Algo salio mal!", "Parece que ocurrió un error, intentalo de nuevo.")
        
#------------------SEPARADOR DE PDFS------------------#    

class separarPdf():
    pdf = None
    def __init__(self) -> None:
        pass    
    
    def abrir(this) -> PyPDF2.PdfFileReader:
        this.pdf = filedialog.askopenfile(filetypes=[("Archivos PDF", "*.pdf")])
        lst.insert(tkinter.END, basename(this.pdf.name))
    
    def separarTodas(this) -> PyPDF2.PdfWriter:
        original = PyPDF2.PdfReader(this.pdf.name)
    
        nombreParaPdfs = filedialog.asksaveasfile(defaultextension=".pdf", filetypes=[("Archivo PDF" , "*.pdf")]).name
    
        for Npagina in range(len(original.pages)):
        
            pdfSeparado = PyPDF2.PdfWriter()
            page = original.pages[Npagina]
            pdfSeparado.add_page(page)

            pdfSeparado.write(f"{nombreParaPdfs}{Npagina+1}.pdf")
    
        tkinter.messagebox.showinfo("FELICIDADES!", "La separacion ha sido todo un exito.".title())
    
    def separarEspecifica(this) -> PyPDF2.PdfWriter:
        original = PyPDF2.PdfReader(this.pdf.name)
        pdfSeparado = PyPDF2.PdfWriter()
        
        
        nombreParaPdfs = filedialog.asksaveasfile(defaultextension=".pdf", filetypes=[("Archivo PDF" , "*.pdf")]).name
        excluidas = []
        
        separar = entrada.get()
        separar.replace(" ", "")
        for i in separar:
            if i.isnumeric():
                excluidas.append(int(i))
            else:
                continue
            
        pagEliminadas = []
            
        for Npagina in range(len(original.pages)):
            
            if Npagina + 1 in excluidas:
                pagEliminadas.append(original.pages[Npagina])
            else:
                if not Npagina +1 in excluidas:
                    page = original.pages[Npagina]
                    pdfSeparado.add_page(page)

        pdfSeparado.write(nombreParaPdfs)
        pdfSeparado.close()
        tkinter.messagebox.showinfo("FELICIDADES!", "La separacion ha sido todo un exito.".title())
        
        
#------------------CAMBIA CONTENIDO DE ROOT------------------#

def cambiaVentana1():
    ventana.grid(column=0,row=1)
    
    framebtnRight.grid_forget()
    framebtn.grid(column=2, row=1)
    
    botonVentana1.grid_forget()
    botonVentana2.grid(column=0, row=0,pady=6)
    root.title("UNE PDFS RAPIDO Y GRATIS")
    
    
def cambiaVentana2():  
    ventana.grid(column=0,row=1)
    
    framebtn.grid_forget()
    framebtnRight.grid(column=2, row=1)
    
    botonVentana2.grid_forget()
    botonVentana1.grid(column=0, row=0,pady=6)
    root.title("SEPARA PDFS RAPIDO Y GRATIS")
    

#De aqui en adelante todo es la interfaz grafica para el usuario.

root = tkinter.Tk()
root.resizable(0,0)
root.title("PDFS RAPIDO Y GRATIS")
root.geometry(f"{root.winfo_reqwidth() + 255}x{root.winfo_reqheight() + 130}+{(root.winfo_screenwidth() - root.winfo_reqwidth()) // 2}+{(root.winfo_screenheight() - root.winfo_reqheight()) // 2}")

ventana = tkinter.Frame()

botonVentana1 = tkinter.Button(root,text="UNIR PDFS RAPIDO", command=cambiaVentana1)
botonVentana2 = tkinter.Button(root,text="SEPARAR PDFS RAPIDO", command=cambiaVentana2)

botonVentana1.grid(column=0, row=0,padx=10,pady=6)
botonVentana2.grid(column=1, row=0,padx=10,pady=6)

#------------------UNIDOR DE PDFS------------------#
label1 = tkinter.Label(ventana, text="Une rapido y gratis tus pdfs", font="Abadi")
label1.grid(column=1, row=0, pady=15)

lst = tkinter.Listbox(ventana, selectmode=tkinter.MULTIPLE, height=13, width=30, border=0, font=("Comic", 8))
lst.grid(column=1, row=1,pady=1)

#frame de los botones a la derecha
framebtn = tkinter.Frame(ventana)
framebtn.grid(column=2, row=1)

#frame de los botones a la izquierda
framebtnleft = tkinter.Frame(ventana)
framebtnleft.grid(column=0, row=1)

#frame de la lista
framelst = tkinter.Frame(ventana)
framelst.grid(column=1, row=2)

#--------------Botones a la derecha--------------

btnAgg = tkinter.Button(framebtn, text="Elige tus pdfs".upper(), border= 4, width= 20, cursor="hand2", command=AggPdf, font=("Abadi", 8) )
btnAgg.grid(column=3, row=1,pady=15)

btnUnir= tkinter.Button(framebtn, text="UNIR".upper(), border= 4, width= 20, cursor="hand2", command=UnirPdf, font=("Abadi", 8) )
btnUnir.grid(column=3, row=2,pady=15)

#--------------Botones a la izquierda--------------

btnadd= tkinter.Button(framebtnleft, text="+".upper(), border= 4, width= 5, cursor="hand2", command=AggPdf, font=("Abadi", 8) )
btnadd.grid(column=0, row=0,pady=10)

btndel= tkinter.Button(framebtnleft, text="-".upper(), border= 4, width= 5, cursor="hand2", command=delLst, font=("Abadi", 8) )
btndel.grid(column=0, row=1,pady=5, padx=10)

#------------------SEPARADOR DE PDFS------------------#

#frame de los botones a la derecha
framebtnRight = tkinter.Frame(ventana)
framebtnRight.grid(column=2, row=1)
separador = separarPdf()
#--------------Botones a la derecha--------------

btnAgg = tkinter.Button(framebtnRight, text="Elige tu pdf".upper(), border= 4, width= 20, cursor="hand2", command=separador.abrir, font=("Abadi", 8) )
btnAgg.grid(column=3, row=1,pady=15)

btnUnir= tkinter.Button(framebtnRight, text="SEPARAR TODO".upper(), border= 4, width= 20, cursor="hand2", command=separador.separarTodas, font=("Abadi", 8) )
btnUnir.grid(column=3, row=2,pady=15)

btnUnir= tkinter.Button(framebtnRight, text="SEPARAR EXCLUYENDO".upper(), border= 4, width= 20, cursor="hand2", command=separador.separarEspecifica, font=("Abadi", 8) )
btnUnir.grid(column=3, row=4,pady=15)

Npagina = tkinter.Label(framebtnRight, text="Nª pagina a excluir:", font=("Abadi", 7))
Npagina.grid(column=3, row=3)

entrada = tkinter.Entry(framebtnRight, width=8)
entrada.grid(column=4, row=3)


root.mainloop()