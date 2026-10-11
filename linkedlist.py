# ============================================================
# Laboratoriya işi №1 - Singly Linked List
# ============================================================

# ---------- Tapşırıq 1: Node sinfi ----------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------- Linked List sinfi ----------
class LinkedList:
    def __init__(self):
        self.head = None

    # Tapşırıq 2: Sonuna əlavə etmə
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Tapşırıq 3: Əvvəlinə əlavə etmə
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Tapşırıq 4: Verilmiş elementdən sonra əlavə etmə
    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        print(f"{target} elementi tapılmadı.")
        return False

    # Tapşırıq 5: Element silmə
    def delete(self, value):
        if self.head is None:
            print("Siyahı boşdur.")
            return False
        # Silinən element head-dirsə
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        print(f"{value} elementi tapılmadı.")
        return False

    # Tapşırıq 6: Axtarış
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False

    # Tapşırıq 7: Uzunluq
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Tapşırıq 8: Maksimum və minimum
    def max_min(self):
        if self.head is None:
            return None, None
        maximum = minimum = self.head.data
        current = self.head.next
        while current:
            if current.data > maximum:
                maximum = current.data
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return maximum, minimum

    # Tapşırıq 9: Tərs çevirmə (yeni siyahı yaradılmır, əlaqələr dəyişdirilir)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Çap etmə
    def display(self):
        current = self.head
        result = ""
        while current:
            result += f"{current.data} -> "
            current = current.next
        print(result + "None")


# ============================================================
# TESTLƏR
# ============================================================

print("=== Tapşırıq 1: Node ===")
n = Node(15)
print("Node data:", n.data, "| next:", n.next)

print("\n=== Tapşırıq 2: Sonuna əlavə ===")
ll = LinkedList()
for x in [10, 20, 30, 40]:
    ll.append(x)
ll.display()

print("\n=== Tapşırıq 3: Əvvəlinə əlavə ===")
ll = LinkedList()
for x in [20, 30, 40]:
    ll.append(x)
ll.prepend(10)
ll.display()

print("\n=== Tapşırıq 4: Elementdən sonra əlavə ===")
ll = LinkedList()
for x in [10, 20, 40]:
    ll.append(x)
ll.insert_after(20, 30)
ll.display()

print("\n=== Tapşırıq 5: Silmə ===")
ll = LinkedList()
for x in [10, 20, 30, 40, 50]:
    ll.append(x)
ll.delete(30)
ll.display()

print("\n=== Tapşırıq 6: Axtarış ===")
ll.search(40)
ll.search(99)

print("\n=== Tapşırıq 7: Uzunluq ===")
ll = LinkedList()
for x in [11, 22, 33, 44, 55]:
    ll.append(x)
print("List length =", ll.length())

print("\n=== Tapşırıq 8: Max və Min ===")
ll = LinkedList()
for x in [23, 8, 91, 15, 42]:
    ll.append(x)
mx, mn = ll.max_min()
print("Maksimum element:", mx)
print("Minimum element:", mn)

print("\n=== Tapşırıq 9: Tərs çevirmə ===")
ll = LinkedList()
for x in [10, 20, 30, 40, 50]:
    ll.append(x)
print("Əvvəl:", end=" ")
ll.display()
ll.reverse()
print("Sonra:", end=" ")
ll.display()


# ============================================================
# Tapşırıq 10 (Challenge): Tələbə qeydiyyat sistemi
# ============================================================

class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # 1. Tələbə əlavə et
    def add_student(self, student_id, name, gpa):
        # Eyni ID yoxlanışı
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"ID {student_id} artıq mövcuddur!")
                return
            current = current.next

        new_node = StudentNode(student_id, name, gpa)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"{name} əlavə edildi.")

    # 2. Tələbə sil (ID-yə görə)
    def remove_student(self, student_id):
        if self.head is None:
            print("Siyahı boşdur.")
            return
        if self.head.student_id == student_id:
            print(f"{self.head.student_name} silindi.")
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.student_id == student_id:
                print(f"{current.next.student_name} silindi.")
                current.next = current.next.next
                return
            current = current.next
        print(f"ID {student_id} olan tələbə tapılmadı.")

    # 3. Bütün tələbələri göstər
    def show_all(self):
        if self.head is None:
            print("Siyahı boşdur.")
            return
        print(f"{'ID':<8}{'Ad':<20}{'GPA':<6}")
        print("-" * 34)
        current = self.head
        while current:
            print(f"{current.student_id:<8}{current.student_name:<20}{current.gpa:<6}")
            current = current.next

    # 4. GPA > 80 olanları göstər
    def show_high_gpa(self, limit=80):
        found = False
        print(f"GPA > {limit} olan tələbələr:")
        current = self.head
        while current:
            if current.gpa > limit:
                print(f"{current.student_id:<8}{current.student_name:<20}{current.gpa:<6}")
                found = True
            current = current.next
        if not found:
            print("Heç bir tələbə tapılmadı.")

    # 5. Ada görə axtarış
    def search_by_name(self, name):
        current = self.head
        found = False
        while current:
            if current.student_name.lower() == name.lower():
                print(f"Tapıldı -> ID: {current.student_id}, Ad: {current.student_name}, GPA: {current.gpa}")
                found = True
            current = current.next
        if not found:
            print("Tələbə tapılmadı.")

    # 6. Tələbələrin sayı
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# ---------- Menyu ----------
def menu():
    students = StudentList()
    # Test üçün hazır məlumatlar (istəsən silə bilərsən)
    students.add_student(1, "Fidan", 92.5)
    students.add_student(2, "Elvin", 78)
    students.add_student(3, "Aysel", 85)

    while True:
        print("\n===== TƏLƏBƏ QEYDİYYAT SİSTEMİ =====")
        print("1. Tələbə əlavə et")
        print("2. Tələbə sil")
        print("3. Bütün tələbələri göstər")
        print("4. GPA > 80 olanları göstər")
        print("5. Ada görə axtarış et")
        print("6. Tələbələrin sayını göstər")
        print("0. Çıxış")
        choice = input("Seçim: ").strip()

        if choice == "1":
            try:
                sid = int(input("Tələbə ID: "))
                name = input("Ad: ").strip()
                gpa = float(input("GPA: "))
                students.add_student(sid, name, gpa)
            except ValueError:
                print("Xəta: ID və GPA rəqəm olmalıdır!")
        elif choice == "2":
            try:
                sid = int(input("Silinəcək tələbənin ID-si: "))
                students.remove_student(sid)
            except ValueError:
                print("Xəta: ID rəqəm olmalıdır!")
        elif choice == "3":
            students.show_all()
        elif choice == "4":
            students.show_high_gpa()
        elif choice == "5":
            name = input("Axtarılan ad: ").strip()
            students.search_by_name(name)
        elif choice == "6":
            print("Tələbələrin sayı:", students.count())
        elif choice == "0":
            print("Proqram bitdi.")
            break
        else:
            print("Yanlış seçim!")


print("\n=== Tapşırıq 10: Tələbə qeydiyyat sistemi ===")
menu()