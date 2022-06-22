from dataclasses import dataclass

# x_lut =  [0, 1, 0, 1, 0, 1, 0, 1]
# y_lut =  [0, 0, 1, 1, 0, 0, 1, 1]
# z_lut = [0, 0, 0, 0, 1, 1, 1, 1]
# i_lut =  [0, 3, 4, 7, 0, 6, 1, 7, 0, 5, 2, 7]
# j_lut = [1, 2, 5, 6, 2, 4, 3, 5, 4, 1, 6, 3]
# k_lut = [3, 0, 7, 4, 6, 0, 7, 1, 5, 0, 7, 2]

x_lut = [0, 0, 1, 1, 0, 0, 1, 1]
y_lut = [0, 1, 1, 0, 0, 1, 1, 0]
z_lut = [0, 0, 0, 0, 1, 1, 1, 1]
i_lut = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
j_lut = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
k_lut = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6]

@dataclass
def MeshBuilder:
    n_verts: int

    faces_i: list
    faces_j: list
    faces_k: list

    verts_x: list
    verts_y: list
    verts_z: list

    def addBox(self, px, py, pz, sx, sy, sz):
        for q in range(12):
            self.faces_i.append(i_lut[q] + self.n_verts)
            self.faces_j.append(j_lut[q] + self.n_verts)
            self.faces_k.append(k_lut[q] + self.n_verts)
        for q in range(8):
            self.verts_x.append(px + sx * x_lut[q])
            self.verts_y.append(py + sy * y_lut[q])
            self.verts_z.append(pz + sz * z_lut[q])
            self.n_verts += 1

