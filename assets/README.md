# assets

custom textures the loader downloads and merges into the in-game dropdowns.

- `beams/` — bullet tracer textures. they show up in **visuals > bullets > tracer texture**.
- `decals/` — forcefield cham textures. they show up in the **decal** dropdown on any
  cham category once its material is set to `forcefield`.

drop `.png`, `.jpg`, `.jpeg` or `.webp` files in either folder. the file name minus its
extension becomes the dropdown entry, so `neon stripe.png` lists as `neon stripe`.

names that collide with a built-in entry are ignored, so pick something distinct.
