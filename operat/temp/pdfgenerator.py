from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #font
        self.set_font('Arial','' ,8)
        # image
        self.image('operat\\temp\\logo_geo.png', 130, 8, 30)
        #left decrption of robota geodezyjna
        self.cell(90, 10,'KERG - ID zgloszenia', 0, 0, 'L')
        self.set_y(15)
        self.cell(90, 10, 'wojewodztwo: ', 0, 0, 'L')
        self.cell(90, 10, 'Geo-Expert Piotr Sieczkiewicz', 0, 0, 'C')
        self.set_y(18)
        self.cell(90, 10,'powiat', 0, 0, 'L')
        self.cell(90, 10, 'ul. Chopina 49a//4, 71-450 Szczecin', 0, 0, 'C')
        self.set_y(21)
        self.cell(90, 10,'jdn. ewid.:', 0, 0, 'L')
        self.cell(90, 10, 'NIP 851-281-33-19, REGON 320402127', 0, 0, 'C')
        self.set_y(24)
        self.cell(90, 10,'obreb:', 0, 0, 'L')
        self.cell(90, 10, 'e-mail: biuro@geo-expert.pl; tel. 601-377-627 ', 0, 0, 'C')
        # line break
        self.ln(20)
    def footer(self):
        #postion from the bottom
        self.set_y(-15)
        #font
        self.set_font('Arial', '', 8)
        #page number
        self.cell(90, 10, str(self.page_no()) , 0, 0, 'R')
        #right information about digital sign
        self.cell(90, 10, 'cyforowo podpisane przez', 0, 0, 'R')
    def body(self, name):
        # dane od użytkownika z pliku
        #with open(name, 'rb') as fh:
        # txt = fh.read().decode('latin-1')
        #czcionka
        self.set_font('Arial', '', 11)
        # wynik jako wyrównany tekst
        self.multi_cell(0, 5, name)
        # linia przerwy
        self.ln()
    def print_body(self):
        self.add_page()
        name = input('Uzupelnij dane:')
        self.body(name)



pdf = PDF('P', 'mm', 'A4')
pdf.alias_nb_pages()
#pdf.add_page()
#pdf.set_font('Arial', '', 12)
#for i in range(1,41):
#    pdf.cell(0, 10, 'Printing line number'+str(i),0, 1)
pdf.print_body()
pdf.output('tuto2.pdf', 'F')