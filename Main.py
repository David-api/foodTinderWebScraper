from scrapers.ScraperMercator import ScraperMercator

def main():
    print("""
    ╱╭━╮╱╱╱╱╱╱╱╭┳━━━━╮╱╱╱╱╭╮╱╱╱╱╭╮╭╮╭╮╱╱╭╮╱╭━━━╮
    ╱┃╭╯╱╱╱╱╱╱╱┃┃╭╮╭╮┃╱╱╱╱┃┃╱╱╱╱┃┃┃┃┃┃╱╱┃┃╱┃╭━╮┃
    ╭╯╰┳━━┳━━┳━╯┣╯┃┃┣╋━╮╭━╯┣━━┳━┫┃┃┃┃┣━━┫╰━┫╰━━┳━━┳━┳━━┳━━┳━━┳━╮
    ╰╮╭┫╭╮┃╭╮┃╭╮┃╱┃┃┣┫╭╮┫╭╮┃┃━┫╭┫╰╯╰╯┃┃━┫╭╮┣━━╮┃╭━┫╭┫╭╮┃╭╮┃┃━┫╭╯
    ╱┃┃┃╰╯┃╰╯┃╰╯┃╱┃┃┃┃┃┃┃╰╯┃┃━┫┃╰╮╭╮╭┫┃━┫╰╯┃╰━╯┃╰━┫┃┃╭╮┃╰╯┃┃━┫┃
    ╱╰╯╰━━┻━━┻━━╯╱╰╯╰┻╯╰┻━━┻━━┻╯╱╰╯╰╯╰━━┻━━┻━━━┻━━┻╯╰╯╰┫╭━┻━━┻╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
    By David Cadez
    
    All output is redirected to output.log
    """)

    scd = ScraperMercator(100, 0, 3);
    scd.work()


if __name__ == "__main__":
    main()
