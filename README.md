- for GPU base on `branch` [v0.4.2](https://github.com/ANTsX/ANTsPy/tree/v0.4.2)

  

### Samples
```
    # 图像配准
    seg_gary = cv.cvtColor(seg, cv.COLOR_BGR2GRAY)

    template_gary = cv.cvtColor(_template_clor, cv.COLOR_BGR2GRAY)
    _template_gary = template_gary.copy()

    moving_image = seg_gary.reshape((width, _h), order="F")
    fixed_image = template_gary.reshape((width, _h), order="F")

    cudaRegistration = utils.get_lib_fn("cudaRegistration")
    Gc = cudaRegistration(fixed_image, moving_image)

    ants_img = Gc.reshape((_h, width), order="F")

    fixed_image = _template_gary.astype(np.uint8)
    ants_img = ants_img.astype(np.uint8)
```
