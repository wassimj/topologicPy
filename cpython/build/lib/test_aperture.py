from . import Aperture

if __name__ == '__main__':
    a = Aperture()
    if a.IsManifold():
        print("Not Manifold")
    else:
        print("It is Manifold")