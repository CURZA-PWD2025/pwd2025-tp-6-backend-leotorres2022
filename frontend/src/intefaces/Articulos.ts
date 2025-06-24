import type { Marca } from "./Marca";
import type { Proveedores } from "./Proveedores";
import type { Categorias } from "./Categorias";
export interface Articulos{
id?: number;
descripcion: string;
precio: number;
stock: number;
marca?: Marca;
proveedor?: Proveedores;
categorias?: Categorias[]
}
