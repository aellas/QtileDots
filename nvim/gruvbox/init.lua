local vim = vim

-- Install lazy.nvim if not already installed
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git", "--branch=stable", lazypath
  })
end
vim.opt.rtp:prepend(lazypath)

-- Load plugins
require("lazy").setup({
  { "olivercederborg/poimandres.nvim", lazy = false, priority = 1000, config = true },
  { "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
  { "nvim-lualine/lualine.nvim", dependencies = { "nvim-tree/nvim-web-devicons" } },
  { "nvim-telescope/telescope.nvim", dependencies = { "nvim-lua/plenary.nvim" } },
  { "neovim/nvim-lspconfig" },
  { "hrsh7th/nvim-cmp", dependencies = { "hrsh7th/cmp-nvim-lsp", "L3MON4D3/LuaSnip" } },
  { "goolord/alpha-nvim", dependencies = { "nvim-tree/nvim-web-devicons" }, config = function()
      local alpha = require("alpha")
      local dashboard = require("alpha.themes.dashboard")

      -- Set header
      dashboard.section.header.val = {
        " ██████╗ ██╗ █████╗ ███╗   ███╗ █████╗ ███╗   ██╗██████╗ ███████╗",
        " ██╔══██╗██║██╔══██╗████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝",
        " ██████╔╝██║███████║██╔████╔██║███████║██╔██╗ ██║██║  ██║███████╗",
        " ██╔═══╝ ██║██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║╚════██║",
        " ██║     ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝███████║",
        " ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝",
      }

      -- Set menu buttons
      dashboard.section.buttons.val = {
        dashboard.button("e", "  New file", ":ene <BAR> startinsert <CR>"),
        dashboard.button("f", "  Find file", ":Telescope find_files hidden=true<CR>"),
        dashboard.button("r", "  Recent files", ":Telescope oldfiles<CR>"),
        dashboard.button("q", "  Quit Neovim", ":qa<CR>"),
      }

      -- Set footer
      dashboard.section.footer.val = { " Happy coding with Neovim!" }

      -- Apply layout
      alpha.setup(dashboard.config)
    end }
})

-- Set colorscheme
vim.cmd.colorscheme("poimandres")

-- Remove tildes (~) on empty lines
vim.opt.fillchars = { eob = " " }

-- Treesitter setup
require("nvim-treesitter.configs").setup {
  ensure_installed = { "lua", "python", "javascript", "html", "css" },
  highlight = { enable = true }
}

-- Lualine setup
require("lualine").setup {
  options = { theme = "poimandres" }
}

-- LSP setup
local lspconfig = require("lspconfig")
lspconfig.lua_ls.setup({})
lspconfig.pyright.setup({})
lspconfig.ts_ls.setup({})

-- Completion setup
local cmp = require("cmp")
cmp.setup {
  mapping = {
    ["<C-Space>"] = cmp.mapping.complete(),
    ["<CR>"] = cmp.mapping.confirm({ select = true })
  },
  sources = cmp.config.sources({
    { name = "nvim_lsp" },
    { name = "luasnip" }
  })
}

-- Telescope configuration to show dotfiles
require("telescope").setup {
  defaults = {
    file_ignore_patterns = {},
    vimgrep_arguments = {
      "rg", "--color=never", "--no-heading", "--with-filename", "--line-number", "--column",
      "--smart-case", "--hidden"
    }
  }
}
vim.api.nvim_set_keymap("n", "<leader>fd", ":Telescope find_files hidden=true<CR>", { noremap = true, silent = true })