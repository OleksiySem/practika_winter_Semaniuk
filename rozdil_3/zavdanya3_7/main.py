import ui
import logic
def main():
    app = ui.MainWindow(process_callback=logic.process_text)
    app.run()
if __name__ == "__main__":
    main()