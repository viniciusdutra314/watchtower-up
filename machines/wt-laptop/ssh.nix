
{ ... }:
{
  programs.ssh = {
    enable = true;
    enableDefaultConfig = false;
    settings = 
      let 
        DefaultIdentityFile="~/.ssh/id_ed25519"; 
      in
      {     
      wt-unlock = {
        HostName = "192.168.0.100";
        User = "root";
        Port = 2222;
        IdentityFile = DefaultIdentityFile;
        IdentitiesOnly = true;
      };
      wt-server = {
        HostName = "wt-server";
        User = "vinicius";
        IdentityFile = DefaultIdentityFile;
        IdentitiesOnly = true;
      };

      wt-dev = {
        HostName = "wt-dev";
        User = "chloe";
        IdentityFile = DefaultIdentityFile;
        IdentitiesOnly = true;
      };
    };
  };
}
