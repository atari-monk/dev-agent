from automation_db.cli.cli import handle_cli, init_cli

def main():
    parser = init_cli()
    args = parser.parse_args()
    handle_cli(args)

if __name__ == "__main__":
    main()
