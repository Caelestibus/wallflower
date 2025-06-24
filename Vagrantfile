Vagrant.configure("2") do |config|
  config.vm.define "attacker" do |attacker|
    attacker.vm.box = "kalilinux/rolling"
    attacker.vm.hostname = "attacker"
    attacker.vm.network "private_network", ip: "192.168.56.10"
    attacker.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end

  config.vm.define "victim" do |victim|
    victim.vm.box = "ubuntu/bionic64"
    victim.vm.hostname = "victim"
    victim.vm.network "private_network", ip: "192.168.56.20"
    victim.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end
end
