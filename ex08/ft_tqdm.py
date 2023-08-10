def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 158

    for i, item in enumerate(lst):
        progress = (i + 1) / total
        block = int(round(bar_length * progress))
        bar = '█' * block + ' ' * (bar_length - block)

        print(f'\r{round(progress*100)}%|{bar}| {i + 1}/{total}',
              end='', flush=True)
        yield item

    print()


if __name__ == "__main__":
    from time import sleep

    for elem in ft_tqdm(range(333)):
        sleep(0.005)

    print()

    from tqdm import tqdm

    for elem in tqdm(range(333)):
        sleep(0.005)

    print()
