for file in ./ek_data/*.tar.gz; do
  fn=$(basename $file)
  fn=${fn/.tar.gz/}
  ls -lah $file
  mkdir -p ek_data/frames/$fn
  tar xf $file --directory=ek_data/frames/$fn
done

rm -fr P01_01.tar.gz