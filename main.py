from vispy import scene
import numpy as np
from vispy.visuals.transforms import MatrixTransform

# Fungsi untuk membuat kubus dengan warna yang benar
def create_hierarchical_cube_visual():
    # Koordinat vertex untuk kubus (8 titik)
    vertices = np.array([
        [-1, -1, -1],  # Titik 0
        [ 1, -1, -1],  # Titik 1
        [ 1,  1, -1],  # Titik 2
        [-1,  1, -1],  # Titik 3
        [-1, -1,  1],  # Titik 4
        [ 1, -1,  1],  # Titik 5
        [ 1,  1,  1],  # Titik 6
        [-1,  1,  1],  # Titik 7
    ])

    # Indeks untuk setiap segitiga pada kubus (12 segitiga)
    faces = np.array([
        [0, 1, 2], [0, 2, 3],  # Sisi bawah
        [4, 5, 6], [4, 6, 7],  # Sisi atas
        [0, 1, 5], [0, 5, 4],  # Sisi depan
        [2, 3, 7], [2, 7, 6],  # Sisi belakang
        [0, 3, 7], [0, 7, 4],  # Sisi kiri
        [1, 2, 6], [1, 6, 5],  # Sisi kanan
    ])

    # Menyediakan 12 warna, satu untuk setiap segitiga
    colors = np.array([
        [1, 0, 0, 1],  # Merah
        [0, 1, 0, 1],  # Hijau
        [0, 0, 1, 1],  # Biru
        [1, 1, 0, 1],  # Kuning
        [1, 0, 1, 1],  # Magenta
        [0, 1, 1, 1],  # Cyan
        [1, 0.5, 0, 1],  # Oranye
        [0.5, 0, 1, 1],  # Ungu
        [0.5, 0.5, 0.5, 1],  # Abu-abu
        [0.25, 0.75, 0.25, 1],  # Hijau terang
        [0.75, 0.25, 0.75, 1],  # Magenta terang
        [0.75, 0.75, 0.25, 1],  # Kuning terang
    ])

    return vertices, faces, colors

# Fungsi untuk menampilkan scene dengan hierarchical cube
def display_scene():
    # Membuat canvas dan menambahkan view
    canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
    view = canvas.central_widget.add_view()

    # Membuat kubus hierarkis
    vertices, faces, colors = create_hierarchical_cube_visual()
    cube_mesh = scene.visuals.Mesh(vertices=vertices, faces=faces, face_colors=colors)

    # Membuat transformasi untuk grup dan objek anak
    group_transform = MatrixTransform()
    group_transform.rotate(45, (0, 1, 0))  # Rotasi 45 derajat pada sumbu Y
    group_transform.translate((0, 0, -10))  # Menggeser kubus ke depan agar terlihat lebih jelas

    # Menambahkan kubus utama dengan transformasi grup
    cube_mesh.transform = group_transform

    # Membuat objek anak dan memberikan transformasi
    child_transform = MatrixTransform()
    child_transform.translate([2, 0, 0])  # Posisi anak lebih jauh dari kubus utama

    # Menambahkan kubus anak
    child_cube = scene.visuals.Mesh(vertices=vertices, faces=faces, face_colors=colors)
    child_cube.transform = child_transform  # Terapkan transformasi ke kubus anak

    # Menambahkan objek-objek tersebut ke dalam view
    view.add(cube_mesh)
    view.add(child_cube)

    # Mengatur kamera untuk melihat objek
    view.camera = scene.cameras.TurntableCamera(fov=45, parent=view.scene)

    # Menampilkan hasil
    canvas.app.run()

if __name__ == "__main__":
    display_scene()
