from vispy import scene
import numpy as np
from vispy.visuals import transforms
from vispy.geometry import MeshData


# Fungsi untuk menggambar piramida (limas) dengan warna berbeda di setiap sisi
def create_pyramid():
    # Koordinat vertice piramida (ukuran lebih besar)
    vertices = np.array([
        [0, 0, 0],  # Titik bawah
        [3, 0, 0],  # Titik kanan
        [3, 3, 0],  # Titik atas kanan
        [0, 3, 0],  # Titik kiri atas
        [1.5, 1.5, 5],  # Titik puncak (lebih tinggi dan lebih besar)
    ])

    # Membuat indeks untuk menghubungkan titik-titik menjadi segitiga
    faces = np.array([
        [0, 1, 4],  # Sisi depan
        [1, 2, 4],  # Sisi kanan
        [2, 3, 4],  # Sisi belakang
        [3, 0, 4],  # Sisi kiri
        [0, 1, 2],  # Dasar depan
        [2, 3, 0]  # Dasar belakang
    ])

    # Warna untuk setiap sisi (RGB)
    colors = np.array([
        [1, 0, 0, 1],  # Merah (sisi depan)
        [0, 1, 0, 1],  # Hijau (sisi kanan)
        [0, 0, 1, 1],  # Biru (sisi belakang)
        [1, 1, 0, 1],  # Kuning (sisi kiri)
        [0.5, 0.5, 0.5, 1],  # Abu-abu (dasar depan)
        [0.5, 0.5, 0.5, 1],  # Abu-abu (dasar belakang)
    ])

    return vertices, faces, colors


# Fungsi untuk membuat visual piramida menggunakan Vispy
def create_pyramid_visual():
    vertices, faces, colors = create_pyramid()

    # Membuat objek Mesh dengan vertices, faces, dan colors
    mesh_visual = scene.visuals.Mesh(vertices=vertices, faces=faces, face_colors=colors)

    return mesh_visual


# Fungsi untuk menampilkan scene dengan transformasi
def display_scene():
    # Membuat canvas untuk visualisasi
    canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
    view = canvas.central_widget.add_view()

    # Membuat visual piramida
    pyramid_visual = create_pyramid_visual()

    # Menambahkan piramida ke scene
    view.add(pyramid_visual)

    # **Modelview Matrix**
    # Transformasi piramida: rotasi dan translasi
    pyramid_visual.transform = transforms.MatrixTransform()
    pyramid_visual.transform.rotate(30, (1, 0, 0))  # Rotasi di sekitar sumbu X
    pyramid_visual.transform.rotate(30, (0, 1, 0))  # Rotasi di sekitar sumbu Y
    pyramid_visual.transform.translate((0, 0, -10))  # Geser objek (model) agar berada dalam ruang tampilan

    # **Projection Matrix**
    # Pengaturan proyeksi perspektif menggunakan kamera dengan field of view (fov) 60 dan distance 10
    view.camera = scene.cameras.TurntableCamera(fov=60, distance=10)

    # **Clip Matrix** - Dikelola secara otomatis oleh kamera di Vispy
    # View frustum otomatis dipotong oleh kamera saat objek berada di luar batas tampilan

    # **Viewport Matrix**
    # Dikelola secara otomatis oleh Vispy, namun Anda dapat mengubah ukuran canvas jika perlu
    canvas.size = (800, 600)  # Ukuran layar

    # Menunggu interaksi pengguna
    canvas.app.run()


if __name__ == "__main__":
    display_scene()
